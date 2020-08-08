from django.db import models
from django.utils import timezone
from datetime import datetime, date 

# Create your models here.
class Webtimer(models.Model):
	title		= models.CharField(max_length=120, null=True)
	urls		= models.CharField(max_length=120, null=True)
	time		= models.DecimalField(decimal_places=3, max_digits=65, null=True) 
	summary		= models.TextField(null=True)
	featured 	= models.BooleanField(default=True, null=True)

	def __str__(self):
		return self.title



class History(models.Model):
	webtimer = models.ForeignKey(Webtimer, null=True, on_delete = models.SET_NULL)
	loadtime = models.DecimalField(decimal_places=3, max_digits=65, null=True)
	captured_date = models.DateTimeField(auto_now_add = False, auto_now = False, null=True)
	
	def save(self, *args, **kwargs):
		if not self.id:
			self.captured_date = datetime.now()

		return super(History, self).save(*args, **kwargs)



