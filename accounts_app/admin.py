from django.contrib import admin
from .models import create_invoice,payment

# Register your models here.

admin.site.register(create_invoice)
admin.site.register(payment)
