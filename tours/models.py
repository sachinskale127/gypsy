from django.db import models

# Create your models here.
class  specialpack(models.Model):
    tourid = models.AutoField
    name = models.CharField(max_length=100,default='')
    img = models.ImageField(upload_to='pics',default='')
    price = models.IntegerField(default='1000')
    days = models.IntegerField(default='5')
    nights = models.IntegerField(default='6')

    def __str__(self):
        return self.name

class  offers(models.Model):
    tourid = models.AutoField
    name = models.CharField(max_length=100,default='')
    img = models.ImageField(upload_to='pics',default='')
    desc = models.CharField(max_length=10000,default='')
    discount = models.IntegerField(default='40')
    actualprice = models.IntegerField(default='6000')
    regularprice = models.IntegerField(default='10000')


    def __str__(self):
        return self.name

class order(models.Model):
    orderid = models.AutoField
    bookingdate = models.DateTimeField(auto_now_add=True)    
    destination =
    member =
    checkin = 
    totalamount =
    firstname = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    email =
    mobile =
    address =
    city =
    pincode =
    state = 

class menu(models.Model):
    destination =
    price =