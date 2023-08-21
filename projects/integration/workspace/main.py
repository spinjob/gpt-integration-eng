from api_integration import APIIntegration
from schedule import Scheduler

def main():
    # Create an instance of the APIIntegration class
    integration = APIIntegration()

    # Create an instance of the Scheduler class
    scheduler = Scheduler()

    # Schedule the integration to run at the specified times
    scheduler.schedule(integration.run, 'weekly', days=['Monday', 'Thursday', 'Saturday'], time='19:00')

if __name__ == "__main__":
    main()
