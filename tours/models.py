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

class  order(models.Model):
    # orderid = models.AutoField
    # bookingdate = models.DateTimeField(auto_now_add=True)    
    # destination = models.CharField(max_length=10000,default='')
    # member = models.IntegerField(max_length=10000,default='1')
    # checkin_day = models.IntegerField(max_length=10000,default='1')
    # checkin_month = models.IntegerField(default='1') 
    # totalamount = models.IntegerField(max_length=10000,default='0')
    firstname = models.CharField(max_length=100,default='')
    lastname = models.CharField(max_length=100,default='')
    email = models.EmailField(max_length = 254)
    mobile = models.IntegerField(max_length=10000,default='')
    Address = models.CharField(max_length=10000,default='')
    Address2 = models.CharField(max_length=400,default='')
    city = models.CharField(max_length=10000,default='')
    pincode = models.IntegerField(max_length=10000,default='')
    state = models.CharField(max_length=10000,default='')


# class menu(models.Model):
#     destination = models.CharField(max_length=10000,default='')
#     price = models.IntegerField(max_length=10000,default='0')