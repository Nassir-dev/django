from django.db import models

# Create your models here.


class create_invoice(models.Model):
    date_created = models.DateField(blank=True, null=True)
    invoice_number = models.CharField(max_length=20,primary_key=True)
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

