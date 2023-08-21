import json
from api import API
from auth import Auth
from workflow import Workflow
from data_mapping import DataMapping

def main():
    # Load the workflow trigger and steps from JSON files
    with open('workflow_trigger.json') as f:
        workflow_trigger = json.load(f)
    with open('workflow_steps.json') as f:
        workflow_steps = json.load(f)

    # Initialize the API and Auth objects
    api = API()
    auth = Auth()

    # Authenticate with the APIs
    auth.authenticate(api)

    # Initialize the Workflow and DataMapping objects
    workflow = Workflow(api)
    data_mapping = DataMapping()

    # Execute the workflow
    workflow.execute(workflow_trigger, workflow_steps, data_mapping)

if __name__ == "__main__":
    main()
