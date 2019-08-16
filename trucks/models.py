from django.db import models
from datetime import date
from client_app.models import Client



    
    

class Trucks(models.Model):
    '''Class to capture all trucks'''
    date_handled=models.DateField(blank=True,null=True )
    truck_no= models.CharField(max_length=50)
    container = models.CharField(max_length=11)
    exporter = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50 , null=True)
    entry_no = models.CharField(max_length=50, primary_key=True)
    
    client = models.ForeignKey(Client,on_delete='CASCADE')
    
    
    
    def __str__(self):
        return self.truck_no




    
        
        
