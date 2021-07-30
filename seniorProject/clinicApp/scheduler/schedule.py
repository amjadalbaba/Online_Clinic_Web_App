import schedule
import time
import logging

logger = logging.getLogger('django')

def job():
    print("I'm working...")

#schedule.every(40).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)

# while 1:
#     schedule.run_pending()
#     time.sleep(1)