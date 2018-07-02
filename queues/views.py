from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	page_context = {}
	return render(request, 'index.html', context=page_context)
	return HttpResponse('Welcome to SmartQueue Prediction System')