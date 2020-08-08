from django.apps import AppConfig


class NetvelotestConfig(AppConfig):
    name = 'netvelotest'
    def ready(self):
    	from netvelotest import updater
    	updater.start()
