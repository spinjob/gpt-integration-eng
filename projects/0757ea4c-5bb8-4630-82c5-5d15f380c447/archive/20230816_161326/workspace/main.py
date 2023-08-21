from api_client import APIClient
from workflow_trigger import WorkflowTrigger
from workflow_step import WorkflowStep
from data_mapper import DataMapper

def main():
    # Create API clients
    pos_api_client = APIClient(
        base_url="https://partners.cloudkitchens.com",
        client_id="04db98cc-0c84-47e2-b57f-bfd6329c4675",
        client_secret="NUCGB6VKFLYQBZPMMBLA",
        scope="menus.get_current menus.publish orders.update storefront.store_availability menus.entity_suspension orders.create",
        grant_type="client_credentials"
    )
    marketplace_api_client = APIClient(
        base_url="https://partners.cloudkitchens.com",
        client_id="be04e745-844d-4a6c-8fba-f71199dc8f05",
        client_secret="MD727PM35KZCWP337TKQ",
        scope="callback.error.write manager.menus manager.orders menus.async_job.read menus.get_current menus.read menus.upsert menus.upsert_hours orders.read ping",
        grant_type="client_credentials"
    )

    # Create data mappers
    create_order_data_mapper = DataMapper({
        # Mapping JSON for Step 1 goes here
    })
    update_order_status_data_mapper = DataMapper({
        # Mapping JSON for Step 2 goes here
    })
    get_menu_data_mapper = DataMapper({
        # Mapping JSON for Step 3 goes here
    })
    publish_error_data_mapper = DataMapper({
        # Mapping JSON for Step 4 goes here
    })

    # Create workflow steps
    steps = [
        WorkflowStep(pos_api_client, create_order_data_mapper),
        WorkflowStep(marketplace_api_client, update_order_status_data_mapper),
        WorkflowStep(pos_api_client, get_menu_data_mapper),
        WorkflowStep(marketplace_api_client, publish_error_data_mapper)
    ]

    # Create workflow trigger
    trigger = WorkflowTrigger(steps)

    # Run the application
    trigger.app.run(debug=True)

if __name__ == "__main__":
    main()
