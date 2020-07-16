from urllib.request import urlopen
from time import time

from .models import History, Webtimer

def update_history():
	try:
		tableone = Webtimer.objects.all()
		loadtime_counter(tableone);
		print('masuk update history')
	except Exception as e:
		print(str(e))


def loadtime_counter(links):
	for link in links:
		try:
			start_time = time()
			stream = urlopen(link.urls)
			output = stream.read()
			end_time = time()
			stream.close()
			elapsed_time = round(end_time-start_time, 3)
		finally:
			link.time = elapsed_time
			link.save()
			new_history = History(webtimer = link, loadtime = link.time)
			new_history.save()