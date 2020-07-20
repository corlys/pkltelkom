from urllib.request import urlopen
from time import time
import threading

from .models import History, Webtimer

def update_history():
	try:
		tableone = Webtimer.objects.all()
		start_time = time()
		# loadtime_counter(tableone)
		start_thread(tableone)
		end_time = time()
		# print(round(end_time-start_time, 3))
	except Exception as e:
		print(str(e))


# def loadtime_counter(links):
# 	for link in links:
# 		try:
# 			start_time = time()
# 			stream = urlopen(link.urls)
# 			output = stream.read()
# 			end_time = time()
# 			stream.close()
# 			elapsed_time = round(end_time-start_time, 3)
# 		finally:
# 			link.time = elapsed_time
# 			link.save()
# 			new_history = History(webtimer = link, loadtime = link.time)
# 			new_history.save()

def loadtime_counter(link):
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

def start_thread(links):
	threads = []
	for link in links:
		t = threading.Thread(target=loadtime_counter, args=(link,))
		threads.append(t)

	for t in threads:
		t.start()

	for t in threads:
		t.join()