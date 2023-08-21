from workflowmanager import WorkflowManager

def main():
    # Create an instance of the WorkflowManager
    manager = WorkflowManager()

    # Start the workflow with a sample webhook body
    webhook_body = {"metadata": {"storeId": "test-store-id"}}
    result = manager.start_workflow(webhook_body)

    return result

if __name__ == "__main__":
    main()
