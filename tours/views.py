from django.shortcuts import render
from django.http import HttpResponse
from .models import specialpack,offers,order
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
    if request.method=="POST":
        #  bookingdate = request.POST.get('bookingdate','')
        #  destination = request.POST.get('destination','')
        #  member = request.POST.get('member','')
        #  checkin_day = request.POST.get('checkin_day','')
        #  checkin_month = request.POST.get('checkin_month','')
         firstname = request.POST.get('firstname','')
         lastname = request.POST.get('lastname','')
         email = request.POST.get('email','')
         mobile = request.POST.get('mobile','')
         Address = request.POST.get('Address','')
         Address2 = request.POST.get('Address2','')
         city = request.POST.get('city','')
         pincode = request.POST.get('pincode','')
         state = request.POST.get('state','')
        #  totalamount = request.POST.get('totalamount','')

         Orders = order(firstname=firstname, lastname=lastname,
                       email=email, mobile=mobile, Address=Address, Address2=Address2, city=city,
                       pincode=pincode, state=state)
        # bookingdate=bookingdate, destination=destination, member=member,totalamount=totalamount
        #                checkin_day=checkin_day, checkin_month=checkin_month,
         Orders.save()
    
    spcl = specialpack.objects.all()
    
    return render(request, 'payment.html',{'spcl':spcl})

def paypal(request):
    return render(request, 'paypal.html')