from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('predictions', views.predictions, name='predictions')
]