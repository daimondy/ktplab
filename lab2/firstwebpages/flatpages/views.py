from django.shortcuts import render
from django.http import HttpResponse
from django import template

def home(request):
	return HttpResponse(u'Привет, Мир!', content_type="text/plain")
# Create your views here.
def home(request):
    return render(request, 'static_handler.html')
