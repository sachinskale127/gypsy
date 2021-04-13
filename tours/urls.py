from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('travelbox/',views.travelbox, name='travelbox'),


]