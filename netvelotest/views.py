import speedtest as st
import csv

from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from datetime import datetime, date 

from .models import Netvelocity, SpeedHistory



# Create your views here.
@login_required(login_url='login')
def netvelocity_view(request):
	obj = Netvelocity.objects.all()

	context = {
		'objects': obj
	}
	return render(request, 'netvelotest/netvelotest_view.html', context)

@login_required(login_url='login')
def netvelocity_history(request):
	format = '%d %B %Y'
	if request.method == 'POST':
		tanggal = request.POST['tanggal']
		datetime_str = datetime.strptime(tanggal, format)
		# print(tanggal)
		hist = SpeedHistory.objects.filter(captured_date__date = datetime_str)
		serv = Netvelocity.objects.all()

		context = {
			'hist':hist,
			'serv':serv
		}
		
		return render(request, 'netvelotest/netvelotest_history.html', context)

	hist = SpeedHistory.objects.filter(captured_date__date = datetime.now())
	serv = Netvelocity.objects.all()

	context = {
		'hist':hist,
		'serv':serv
	}

	return render(request, 'netvelotest/netvelotest_history.html', context)

@login_required(login_url='login')
def export_speedtest_history_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="speedtest-history.csv"'

    writer = csv.writer(response)
    writer.writerow(['id history', 'id server', 'server', 'download', 'upload', 'PING', 'ISP', 'date'])

    users = SpeedHistory.objects.all().values_list('id','speedtest_server__server', 'speedtest_server__name', 'download', 'upload', 'ping', 'isp', 'captured_date' )
    for user in users:
        writer.writerow(user)

    return response

def speed_count(request):
	if request.method == 'GET':
		print(request.GET['server'])
		server_id = request.GET['server']
		obj = Netvelocity.objects.filter(server = server_id)
		for item in obj:
			test = st.Speedtest()
			server = [item.server]
			test.get_servers(server)
			data = {
				"download":round(test.download()/1000000),
				"upload":round(test.upload()/1000000),
				"ping":round(test.results.ping),
				"isp":test.results.client['isp']
			}
			return JsonResponse(data)
