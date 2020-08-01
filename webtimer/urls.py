from django.urls import path
from . import views

urlpatterns = [
	path('', views.apiOverview, name='api-overview'),
	path('web-list/', views.webList, name='web-list'),
	path('web-detail/<str:pk>/', views.webDetail, name='web-detail'),
	path('web-create/', views.webCreate, name='web-create'),
	
	path('web-update/<str:pk>/', views.webUpdate, name="web-update"),
	path('web-delete/<str:pk>/', views.webDelete, name="web-delete"),
]