from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *





# Create your views here.


def indexview(request):
    return render(request,'trucks/begin.html')

def homepage(request):
    trucks = Trucks.objects.order_by('date_handled')
    ashiley = Client.objects.filter(name__exact='Ashiley').count()
    context = {'trucks':trucks, 'ashiley':ashiley}
    return render(request, 'trucks/index.html',context)

def aboutpage(request):
    return render(request, 'trucks/about.html')

def contactme(request):
    clients = Client.objects.order_by('name')
    context = {'clients':clients}
    return render(request, 'trucks/contact.html',context)

def accounts(request):
    return render(request, 'trucks/accounts.html')



def invoice(request):
    #create a new message 
    if request.method != 'POST':
    #create a blank form

        form = InvoiceForm()

    else:
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request,'trucks/create_invoice.html', context)


                
            
        
