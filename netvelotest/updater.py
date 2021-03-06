from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from netvelotest import history_job


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(history_job.update_history, "interval", minutes=5)
    scheduler.start()

