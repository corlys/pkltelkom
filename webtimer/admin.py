from django.contrib import admin

# Register your models here.
from .models import Webtimer, History

admin.site.register(Webtimer)

admin.site.register(History)