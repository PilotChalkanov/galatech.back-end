from django.contrib import admin
from .models import GalaTechUser, GalaTechProfile

# Register your models here.

admin.site.register(GalaTechUser)
admin.site.register(GalaTechProfile)