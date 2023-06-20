from django.contrib import admin
from .models import Person, Car, Client
# Register your models here.

admin.site.register(Person)
admin.site.register(Car)
admin.site.register(Client)
