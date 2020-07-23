from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.core import serializers

from .models import *
from .forms import CreateUserForm
from .decorators import unauthenticated_user
# from .forms import WebtimerForm, RawWebtimerForm

# WebVisit.py Danar

# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait

import urllib.request as urllib2
from time import time

# Create your views here.
@login_required(login_url='login')
def web_timer_home_view(request):
	# w_driver = r"\geckodriver.exe"
	# PATH = r"C:\Users\Duscae\Documents\Python Scripts"
	# driver = webdriver.Firefox()

	obj = Webtimer.objects.all()


	# for link in obj:
	#     try:
	#         driver.get(link.urls)
	#         # Baris ini digunakan untuk membuat pembukaan web menunggu sampai terjadinya domComplete
	#         wait = WebDriverWait(driver, 5).until(
	#          lambda driver: driver.execute_script('return document.readyState') == 'complete'
	#         )
	#         # Baris ini digunakan untuk mengambil waktu respone dimulai dan waktu content selesai diload lalu dikalkulasi untuk mendapatkan total waktu akses
	#         responseStart = driver.execute_script("return window.performance.timing.responseStart")
	#         domComplete = driver.execute_script("return window.performance.timing.domComplete")
	#         frontendPerformance_calc = ((domComplete-responseStart)/3600)
	#     finally:
	#         # print("Waktu yang Dibutuhkan " +link[1]+ " untuk load adalah %.3f detik" %frontendPerformance_calc)
	#         link.time = frontendPerformance_calc

	# driver.close()

	context = {
		'objects' : obj,
	}
	return render(request, 'webtimer/webtimer_home.html', context)

def request_home(request):
	obj = Webtimer.objects.all()
	loadtime_counter(obj);

	data = serializers.serialize('json', obj)

	return HttpResponse(data, content_type="application/json")


@login_required(login_url='login')
def web_timer_history_view(request):
	obj = History.objects.all()
	objects = Webtimer.objects.all()

	context = {
		'hist':obj,
		'web':objects
	}

	return render(request, "webtimer/webtimer_history.html", context)

def web_detail_view(request):
	obj = Webtimer.objects.all()
	if request.method == "GET":
		get_objects = request.GET
	context = {
		'objects':get_objects
	}
	return render(request, 'webtimer/webtimer_detail.html', context)

# def web_detail_create_view(request):

# 	form = WebtimerForm(request.POST)
# 	if form.is_valid():
# 		form.save()
# 		print(request.POST)
# 		form = WebtimerForm(request.POST)

# 	obj = Webtimer.objects.get(id=1)
# 	context = {
# 		'form' : form
# 	}
# 	return render(request, 'webtimer/webtimer_create.html', context)

# def web_detail_create_view(request):
# 	form = RawWebtimerForm()
# 	if request.method == "POST":
# 		form = RawWebtimerForm(request.POST)
# 		if form.is_valid():
# 			form.save()

# 	# obj = Webtimer.objects.get(id=1)
# 	context = {
# 		'form' : form
# 	}
# 	return render(request, 'webtimer/webtimer_create.html', context)		

# Suplimentary Methods

def loadtime_counter(links):
	# http = urllib3.PoolManager()
	for link in links:
		try:
			# http = urllib3.PoolManager()
			# url = 'http://www.thefamouspeople.com/singers.php'
			# stream = http.request('GET', link.urls)
			stream = urllib2.urlopen(link.urls)
			start_time = time()
			output = stream.read()
			end_time = time()
			stream.close()
			elapsed_time = round(end_time-start_time, 3)
		finally:
			link.time = elapsed_time
			link.save()

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('homepage')
		else:
			messages.info(request, 'Username or Password is incorrect')

	context = {}
	return render(request, 'webtimer/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')

@unauthenticated_user
def registerPage(request):
	
	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			saving = form.save()
			group = Group.objects.get(name='costumer')
			saving.groups.add(group)
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for '+ user)
			return redirect('login')
	context = {"form":form}
	return render(request, 'webtimer/register.html', context)