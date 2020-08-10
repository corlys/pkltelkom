from urllib.request import urlopen
from time import time
import threading

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

from .models import History, Webtimer

def update_history():
    try:
        tableone = Webtimer.objects.all()
        start_time = time()
        withthread_counter(tableone)
        end_time = time()


        print(round(end_time-start_time, 3))
    except Exception as e:
        print(str(e))


def nothread_counter(links):
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

def use_browser(link):
    try:
        fireFoxOptions = webdriver.FirefoxOptions()
        fireFoxOptions.set_headless()
        driver = webdriver.Firefox(firefox_options=fireFoxOptions)
        driver.get(link.urls)
        # Baris ini digunakan untuk membuat pembukaan web menunggu sampai terjadinya domComplete
        wait = WebDriverWait(driver, 5).until(
         lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
        # Baris ini digunakan untuk mengambil waktu respone dimulai dan waktu content selesai diload lalu dikalkulasi untuk mendapatkan total waktu akses
        responseStart = driver.execute_script("return window.performance.timing.responseStart")
        domComplete = driver.execute_script("return window.performance.timing.domComplete")
        frontendPerformance_calc = ((domComplete-responseStart)/3600)
    finally:
        # print("Waktu yang Dibutuhkan " +link[1]+ " untuk load adalah %.3f detik" %frontendPerformance_calc)
        link.time = frontendPerformance_calc
        link.save()
        new_history = History(webtimer = link, loadtime = link.time)
        new_history.save()
        driver.close()
    

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

def withthread_counter(links):
    threads = []
    for link in links:
        # kalau mau pakai browser / selenium ganti method targe jadi use_browser
        t = threading.Thread(target=loadtime_counter, args=(link,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()