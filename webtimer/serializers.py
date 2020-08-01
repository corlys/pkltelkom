from rest_framework import serializers
from .models import Webtimer

class WebSerializer(serializers.ModelSerializer):
	class Meta:
		model = Webtimer
		fields ='__all__'