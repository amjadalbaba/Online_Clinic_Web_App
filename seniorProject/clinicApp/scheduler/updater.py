from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from .schedule import job

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, 'interval', seconds=1)
    scheduler.start()
