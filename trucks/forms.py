from django import forms
from .models import *

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields=['name']
        labels={'name':''}

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = create_invoice
        fields = ['date_created','invoice_number','client','month','created_by']
        labels = {'date_created':'Date Created',
                  'invoice_number':'Invoice number',
                  'client':'Client',
                  'month':'Month',
                  'created_by':'Created By'
        }