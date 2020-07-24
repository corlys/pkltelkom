from django.db import models

# Create your models here.
class Netvelocity(models.Model):
	name = models.CharField(max_length=120, null=True)
	server = models.DecimalField(decimal_places=3, max_digits=65, null=True) 
