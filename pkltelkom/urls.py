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
from django.urls import path

from webtimer.views import web_detail_view, web_timer_home_view, web_timer_history_view, request_home
from netvelotest.views import netvelocity_view, speed_count

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', web_timer_home_view),
    path('request_home/', request_home),
    # path('web-create/', web_detail_create_view),
    path('web-detail/', web_detail_view),
    path('web-history/', web_timer_history_view),
    path('speedtest/', netvelocity_view),
    path('speedtest/speed_count', speed_count),
]
