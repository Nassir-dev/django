from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Trucks(models.Model):
    '''Class to capture all trucks'''
    
    truck_no= models.CharField(max_length=50)
    container = models.CharField(max_length=7)
    exporter = models.CharField(max_length=50, default='cleared')
    description = models.CharField(max_length=50 , default='cleared')
    entry_no = models.CharField(max_length=50)
    client = models.ForeignKey(Client,on_delete='CASCADE')
    
    
    def __str__(self):
        return self.truck_no
    
        
        
