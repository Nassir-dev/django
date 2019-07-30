from django.db import models
from datetime import *


class Client(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Trucks(models.Model):
    '''Class to capture all trucks'''
    date_handled=models.DateField(blank=True,null=True )
    truck_no= models.CharField(max_length=50)
    container = models.CharField(max_length=11)
    exporter = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=50 , null=True)
    entry_no = models.CharField(max_length=50)
    client = models.ForeignKey(Client,on_delete='CASCADE')
    
    
    
    def __str__(self):
        return self.truck_no

class create_invoice(models.Model):
    date_created = models.DateField(blank=True, null=True)
    invoice_number = models.CharField(max_length=20)
    client = models.ForeignKey(Client,on_delete='CASCADE')
    month = models.CharField(max_length=50,blank=True)
    amount = models.CharField(max_length=50)
    created_by = models.CharField(max_length=20)

    def __str__(self):
        return self.invoice_number

class payment(models.Model):
    date_created = models.DateField(blank=True, null=True)
    
    invoice_paid = models.ForeignKey(create_invoice, on_delete='CASCADE')
    amount_paid = models.CharField(max_length=50)
    
    def __str__(self):
        return self.invoice_number



    
        
        
