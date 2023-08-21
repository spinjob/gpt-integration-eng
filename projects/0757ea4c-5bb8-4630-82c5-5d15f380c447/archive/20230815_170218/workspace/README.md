The architecture of the application will consist of the following core classes and functions:

1. `APIClient`: This class will be responsible for making HTTP requests to the APIs. It will have methods for each type of request (GET, POST, etc.) and will handle authentication.

2. `OAuth2ClientCredentials`: This class will handle the OAuth2 client credentials flow for both APIs. It will have methods to generate and refresh access tokens.

3. `WorkflowTrigger`: This class will handle the triggering of the workflow. It will have a method to listen for the webhook and start the workflow.

4. `WorkflowStep`: This class will represent a step in the workflow. It will have methods to execute the step and handle the data mapping.

5. `DataMapper`: This class will handle the data mapping for each step. It will have methods to apply the formulas and map the data from the input to the output.

6. `Formula`: This class will represent a formula to be applied in the data mapping. It will have methods to execute the formula.

7. `main`: This function will be the entry point of the application. It will initialize the classes and start the workflow trigger.

Now, let's implement these classes and functions in Python.

`requirements.txt`
