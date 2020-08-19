from time import time
import threading
import speedtest as st


from .models import SpeedHistory, Netvelocity


def update_history():
    try:
        tableone = Netvelocity.objects.all()
        start_time = time()
        # loadtime_counter(tableone)
        start_thread(tableone)
        end_time = time()
        # print(round(end_time-start_time, 3))
    except Exception as e:
        print(str(e))


def nonthreadspeedtest(links):
    for link in links:
        server_id = link.server
        obj = Netvelocity.objects.filter(server=server_id)
        for item in obj:
            test = st.Speedtest()
            server = [item.server]
            test.get_servers(server)
            new_history = SpeedHistory(
                speedtest_server=link,
                download=round(test.download() / 1000000),
                upload=round(test.upload() / 1000000),
                ping=round(test.results.ping),
                isp=test.results.client["isp"],
            )
            new_history.save()


def speedtest_counter(link):
    server_id = link.server
    obj = Netvelocity.objects.filter(server=server_id)
    for item in obj:
        test = st.Speedtest()
        server = [item.server]
        test.get_servers(server)
        new_history = SpeedHistory(
            speedtest_server=link,
            download=round(test.download() / 1000000),
            upload=round(test.upload() / 1000000),
            ping=round(test.results.ping),
            isp=test.results.client["isp"],
        )
        new_history.save()


def start_thread(links):
    threads = []
    for link in links:
        t = threading.Thread(target=speedtest_counter, args=(link,))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

