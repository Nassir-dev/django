from django import ModelForms
from .models import Trucks

class NewTruckForm(froms.ModelForms):
    class Meta:
        model: Trucks
        fields: ['entry_no','truck_no','conatiner','client']
        labels:{'entry_no':'Entry Number','truck_no':'Truck','Container':'Container','client':'Client'}
    