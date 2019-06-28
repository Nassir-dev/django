from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Trucks(models.Model):
    '''Class to capture all trucks'''
    date = models.CharField(max_length=8, default='')
    truck_no= models.CharField(max_length=50)
    container = models.CharField(max_length=7)
    exporter = models.CharField(max_length=50, default='')
    description = models.CharField(max_length=50 , default='')
    entry_no = models.CharField(max_length=50)
    client = models.ForeignKey(Client,on_delete='CASCADE')
    
    
    def __str__(self):
        return self.truck_no

class payments(models.Model):
    
    invoice_paid = models.CharField(max_length=8)
    date_paid = models.CharField(max_length=8)
    amount_paid = models.CharField(max_length=100)
    paid_by = models.CharField(max_length=10)
    balance = models.CharField(max_length=100)
    
        
        
