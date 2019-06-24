from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from . import models
from .forms import NewTruckForm

# Create your views here.


def indexview(request):
    return HttpResponse("Hello this is the Index page")

def homepage(request):
    return HttpResponse("Home page")

def aboutpage(request):
    return HttpResponse("this is the about page call me now")

def contactme(request):
    return HttpResponse("This is the contact us page")

def accounts(request):
    return HttpResponse("This will be the accounts page")

def newtruck(request):
    if request.method!='POST':
        #create a blank 
        form = NewTruckForm()
        
    else:
            #submit to form
            form = NewTruckForm(request.POST)
            if form.is_valid:
                form.save()
                return HttpResponseRedirect(reverse('trucks:Trucks'))

                
            
        
    
