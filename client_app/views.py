from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Client
from .forms import ClientForm

# Create your views here.


def contactme(request):
    clients = Client.objects.order_by('name')
    context = {'clients':clients}
    return render(request, 'trucks/contact.html',context)


def newclient(request):
    #add a new topic
    if request.method != 'POST':
        #create a blank form
        form = ClientForm()
        
    else:
            form = ClientForm(request.POST)
            if form.is_valid():
                form.save()
                
            
    context = {'form':form}
    return render(request,'trucks/newclient.html',context)
