from django.contrib import admin
from trucks.models import Client,Trucks,create_invoice,payment

# Register your models here.

admin.site.register(Client)
admin.site.register(Trucks)
admin.site.register(create_invoice)
admin.site.register(payment)
