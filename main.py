import logging

from pathlib import Path

import typer
from datetime import datetime

from gpt_engineer.ai import AI, fallback_model
from gpt_engineer.collect import collect_learnings
from gpt_engineer.db import DB, DBs, archive
from gpt_engineer.learning import collect_consent
from gpt_engineer.steps import STEPS, Config as StepsConfig

from flask import Flask, request, jsonify
from flask_pymongo import MongoClient
from gridfs import GridFSBucket
import os
from dotenv import load_dotenv

load_dotenv()


# app = typer.Typer()
app = Flask(__name__)

# @app.command()

@app.route('/generate', methods=['POST'])

def generate():
    # Extract parameters from the request
    project_path = request.json.get('project_path', 'projects/example')
    model = request.json.get('model', 'gpt-4')
    temperature = request.json.get('temperature', 0.1)
    project_prompt = request.json.get('project_prompt')
    metadata = request.json.get('metadata')
    steps_config = StepsConfig.TDD

    # Connect to GridFS
    gridfs_db = MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING")).get_database("gpt-engineer")
    gridfs_bucket = GridFSBucket(gridfs_db)

    # Determine the next version number for the given workflow_id project
    workflow_id = metadata.get('workflow_id')
    next_version = get_next_version(gridfs_bucket, workflow_id)

    # Add versioning information to metadata
    metadata["version"] = next_version
    metadata["date"] = str(datetime.now())

    # If the project_path doesn't exist, create it
    Path(project_path).mkdir(parents=True, exist_ok=True)

    # Once the directory exists, add a prompt file and set the contents to the project_prompt text
    with open(Path(project_path) / "prompt", "w") as f:
        f.write(project_prompt)

    # Call the existing main function with the parameters
    return  main(project_path, model, temperature,project_prompt, metadata, steps_config)

def get_next_version(gridfs_bucket, workflow_id):
    # Query existing files for the given workflow_id
    cursor = gridfs_bucket.find({"metadata.workflow_id": workflow_id})

    # Determine the maximum version number.  If no files exist, default to 0
    max_version = max((file.metadata.get("version", 0) for file in cursor), default=0)

    # Return the next version number
    return max_version + 1

def main(
    project_path: str = typer.Argument("projects/example", help="path"),
    model: str = typer.Argument("gpt-4", help="model id string"),
    temperature: float = 0.1,
    project_prompt: str = None,
    metadata: dict = None,
    steps_config: StepsConfig = typer.Option(
        StepsConfig.DEFAULT, "--steps", "-s", help="decide which steps to run"
    ),
    verbose: bool = typer.Option(False, "--verbose", "-v"),
):
    logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)

    print(f"Running with project_prompt={project_prompt}")

    model = fallback_model(model)
    ai = AI(
        model_name=model,
        temperature=temperature,
    )

    input_path = Path(project_path).absolute()
    memory_path = input_path / "memory"
    workspace_path = input_path / "workspace"
    archive_path = input_path / "archive"

    dbs = DBs(
        memory=DB(memory_path),
        logs=DB(memory_path / "logs"),
        input=DB(input_path),
        workspace=DB(workspace_path),
        preprompts=DB(Path(__file__).parent / "preprompts"),
        archive=DB(archive_path),
    )

    if steps_config not in [
        StepsConfig.EXECUTE_ONLY,
        StepsConfig.USE_FEEDBACK,
        StepsConfig.EVALUATE,
    ]:
        archive(dbs)

    steps = STEPS[steps_config]
    for step in steps:
        messages = step(ai, dbs, project_prompt)
        dbs.logs[step.__name__] = AI.serialize_messages(messages)

    # Save Files to GridFS
    file_db_path = dbs.workspace.path
    gridfs_db = MongoClient(os.getenv("MONGO_DB_CONNECTION_STRING")).get_database("gpt-engineer")
    gridfs_bucket = GridFSBucket(gridfs_db)
    dbs.save_files_to_gridfs(file_db_path, gridfs_bucket,metadata)

    # Commented out for now, as the size of the learning data can be too large when the workflow is complex.
    # if collect_consent():
    #     collect_learnings(model, temperature, steps, dbs)

    # Return the amount of tokens used by the LLM for this project_prompt
    token_usage = ai.format_token_usage_log()
    dbs.logs["token_usage"] = token_usage

    return jsonify({"status": "success", "tokens_used": token_usage})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000)  # Adjust host and port as needed