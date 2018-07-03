from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	page_context = {
		'title': 'Dashboard',
		'show_title_on_page': False
	}
	return render(request, 'index.html', context=page_context)

def predictions(request):
	page_context = {
		'title': 'Predictions',
		'show_title_on_page': False
	}

	return render(request, 'predictions.html', context=page_context)