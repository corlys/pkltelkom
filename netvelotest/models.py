from django.db import models
from django.utils import timezone
from datetime import datetime, date 

# Create your models here.
class Netvelocity(models.Model):
	name = models.CharField(max_length=120, null=True)
	server = models.DecimalField(decimal_places=3, max_digits=65, null=True)
	featured 	= models.BooleanField(default=True, null=True)

	def __str__(self):
		return self.name



class SpeedHistory(models.Model):
	speedtest_server = models.ForeignKey(Netvelocity, null=True, on_delete = models.SET_NULL)
	download = models.DecimalField(decimal_places=3, max_digits=65, null=True)
	upload = models.DecimalField(decimal_places=3, max_digits=65, null=True)
	ping = models.DecimalField(decimal_places=3, max_digits=65, null=True)
	isp = models.CharField(max_length=120, null=True)
	captured_date = models.DateTimeField(auto_now_add = False, auto_now = False, null=True)

	def save(self, *args, **kwargs):
		if not self.id:
			self.captured_date = datetime.now()

			return super(SpeedHistory, self).save(*args, **kwargs)
