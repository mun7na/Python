import schedule
import zulu
import datetime
import time

ab = zulu.now()
def job():
    print("A Simple Python Scheduler.", ab)

# run the function job() every 2 seconds
#schedule.every(2).seconds.do(job)
schedule.every().day.at("09:58").do(job)
while True:
    schedule.run_pending()
    time.sleep(10)



