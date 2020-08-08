from django.contrib import admin

# Register your models here.
from .models import Netvelocity, SpeedHistory

admin.site.register(Netvelocity)

admin.site.register(SpeedHistory)