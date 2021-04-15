from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('travelbox/',views.travelbox, name='travelbox'),
    path('success/',views.success, name='success'),
    path('payment/',views.payment, name='payment'),
    path('paypal/',views.paypal, name='paypal'),

]