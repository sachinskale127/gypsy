from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def travelbox(request):
    return render(request, 'travelbox.html')

def aboutus(request):
    return render(request, 'aboutus.html')