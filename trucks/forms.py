from django import forms
from .models import Trucks

class NewTruckForm(forms.ModelForm):
    class Meta:
        model: Trucks
        fields: ['entry_no','truck_no','conatiner','client']
        labels:{'entry_no':'Entry Number','truck_no':'Truck','Container':'Container','client':'Client'}
    