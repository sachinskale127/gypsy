from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('travelbox/',views.travelbox, name='travelbox'),
    path('aboutus/',views.aboutus, name='aboutus'),


]