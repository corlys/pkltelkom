from django.apps import AppConfig


class WebtimerConfig(AppConfig):
    name = 'webtimer'

    def ready(self):
    	from webtimer import updater
    	updater.start()


    	# if ever error indent, ketik sendiri jangan langsung copas
    