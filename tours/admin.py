from django.contrib import admin
# Register your models here.
from .models import specialpack,offers,order

admin.site.register(specialpack)

admin.site.register(offers)

admin.site.register(order)