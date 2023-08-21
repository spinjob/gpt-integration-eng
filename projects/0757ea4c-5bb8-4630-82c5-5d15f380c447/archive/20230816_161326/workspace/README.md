The architecture of the application will consist of the following core classes and functions:

1. `APIClient`: This class will be responsible for making HTTP requests to the APIs. It will include methods for each type of request (GET, POST, etc.) and will handle authentication.

2. `WorkflowTrigger`: This class will be responsible for triggering the workflow. It will include a method to receive the webhook and start the workflow.

3. `WorkflowStep`: This class will represent a single step in the workflow. It will include methods to execute the step, including making the necessary API request and handling the response.

4. `DataMapper`: This class will be responsible for mapping data between steps. It will include methods to extract data from the input, apply any necessary transformations, and insert the data into the output.

5. `main`: This function will be the entry point for the application. It will create instances of the above classes and execute the workflow.

Now, let's implement these classes and functions in Python.

`requirements.txt`
