import schedule
import time

class Scheduler:
    def schedule(self, job, frequency, days, time):
        # Schedule the job to run at the specified frequency, days, and time
        for day in days:
            schedule.every().day.at(time).do(job)

        # Keep the script running
        while True:
            schedule.run_pending()
            time.sleep(1)
