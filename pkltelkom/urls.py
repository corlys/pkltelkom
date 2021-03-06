"""pkltelkom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from webtimer.views import web_detail_view, web_timer_home_view, web_timer_history_view, request_home, loginPage, logoutUser, registerPage, export_web_history_csv
from netvelotest.views import netvelocity_view, speed_count, netvelocity_history, export_speedtest_history_csv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_timer_home_view, name="homepage"),
    path('request_home/', request_home),
    # path('web-create/', web_detail_create_view),
    path('web-detail/', web_detail_view),
    path('web-history/', web_timer_history_view, name="history"),
    path('speedtest/', netvelocity_view, name="speedtest"),
    path('speedtest-history/', netvelocity_history, name="speedtest-history"),
    path('speedtest/speed_count', speed_count),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('api/', include('webtimer.urls')),
    path('export/loadtime', export_web_history_csv, name='export-loadtime-csv'),
    path('export/speedtest', export_speedtest_history_csv, name='export-speedtest-csv'),
]
