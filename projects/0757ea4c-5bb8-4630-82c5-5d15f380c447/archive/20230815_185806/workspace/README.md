The architecture of this application will be divided into several Python files, each responsible for a specific functionality. The main files will be:

1. `main.py`: This will be the entry point of the application. It will handle the webhook trigger and orchestrate the workflow steps.

2. `api_client.py`: This file will contain the `APIClient` class, which will be responsible for making HTTP requests to the APIs.

3. `auth.py`: This file will contain the `OAuth2` class, which will handle the OAuth2 authentication for the APIs.

4. `data_mapper.py`: This file will contain the `DataMapper` class, which will handle the data mapping between each step according to the provided JSON.

5. `formulas.py`: This file will contain the implementation of the formulas used in the data mapping.

6. `requirements.txt`: This file will list all the Python packages required to run the application.

Let's start with the `main.py` file:

main.py
