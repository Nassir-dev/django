from django.shortcuts import render
from django.http import HttpResponse
from .models import *





# Create your views here.


def indexview(request):
    return render(request,'trucks/begin.html')

def homepage(request):
    trucks = Trucks.objects.order_by('truck_no')
    context = {'trucks':trucks}
    return render(request, 'trucks/index.html',context)

def aboutpage(request):
    return render(request, 'trucks/about.html')

def contactme(request):
    clients = Client.objects.order_by('name')
    context = {'clients':clients}
    return render(request, 'trucks/contact.html',context)

def accounts(request):
    return render(request, 'trucks/accounts.html')


                
            
        
