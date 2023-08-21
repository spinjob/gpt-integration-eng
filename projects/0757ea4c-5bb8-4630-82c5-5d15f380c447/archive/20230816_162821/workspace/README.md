The architecture of the application will consist of the following core classes and functions:

1. `APIClient`: This class will be responsible for making HTTP requests to the APIs. It will include methods for each type of request (GET, POST, etc.) and will handle authentication.

2. `OAuth2Client`: This class will inherit from `APIClient` and will implement the OAuth2 authentication scheme.

3. `WorkflowTrigger`: This class will define the condition required to run the application. It will include a method to check if the condition is met.

4. `WorkflowStep`: This class will represent a step in the workflow. It will include a method to execute the step, which will involve making an API request and handling the response.

5. `DataMapper`: This class will handle the mapping of data between steps. It will include methods to extract data from a source (such as a webhook request body or a previous step's response body), apply any necessary transformations, and insert the data into the target location.

6. `Formula`: This class will represent a transformation to be applied to a data value. It will include a method to execute the transformation.

7. `Workflow`: This class will represent the entire workflow. It will include methods to add steps, execute the workflow, and handle errors.

8. `main`: This function will be the entry point for the application. It will create an instance of `Workflow`, add the necessary steps, and execute the workflow.

Now, let's implement these classes and functions in Python.

`requirements.txt`
