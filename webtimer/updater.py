
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from webtimer import history_job

def start():
	scheduler = BackgroundScheduler()
	scheduler.add_job(history_job.update_history, 'interval', hours=1)
	scheduler.start()
