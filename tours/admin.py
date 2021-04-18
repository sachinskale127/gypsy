from django.contrib import admin
# Register your models here.
from .models import specialpack,offers,order,menu

admin.site.register(specialpack)

admin.site.register(offers)

admin.site.register(order)

admin.site.register(menu)