from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    

class Trucks(models.Model):
    '''Class to capture all trucks'''
    entry_no = models.CharField(max_length=50)
    truck_no= models.CharField(max_length=50)
    container = models.CharField(max_length=50)
    client = models.ForeignKey(Client,on_delete='CASCADE')
    
    def __str__(self):
        return self.container
    
        
        
