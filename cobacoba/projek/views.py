from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def index(request):
    return render(request, 'index.html')

