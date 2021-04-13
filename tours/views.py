from django.shortcuts import render
from django.http import HttpResponse
from .models import specialpack,offers

# Create your views here.

def index(request):
    
    spcl = specialpack.objects.all()
    offer = offers.objects.all()
    return render(request,'index.html', {'spcl': spcl,'offer':offer})

def aboutus(request):
    return render(request,'aboutus.html')

def travelbox(request):
    return render(request, 'travelbox.html')