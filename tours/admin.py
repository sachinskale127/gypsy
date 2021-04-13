from django.contrib import admin
# Register your models here.
from .models import specialpack
from .models import offers

admin.site.register(specialpack)

admin.site.register(offers)