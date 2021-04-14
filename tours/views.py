from django.shortcuts import render
from django.http import HttpResponse
from .models import specialpack,offers
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.

def index(request):
    
    spcl = specialpack.objects.all()
    offer = offers.objects.all()
    return render(request,'index.html', {'spcl': spcl,'offer':offer})

def aboutus(request):
    return render(request,'aboutus.html')

def travelbox(request):
    spcl = specialpack.objects.all()
    return render(request, 'travelbox.html', {'spcl': spcl})

def success(request):
    template =  render_to_string('email_template.html')
    
    email = EmailMessage(
        'Booking Confirmed',
        template,
        settings.EMAIL_HOST_USER,
        ['suradkarsantosh1@gmail.com'],
        )
    
    email.fail_silenty=False
    email.send()

    return render(request, 'success.html')

def payment(request):
    return render(request, 'payment.html')
