from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *





# Create your views here.
def homepage(request):
    trucks = Trucks.objects.order_by('date_handled')
    context = {'trucks':trucks, 'ashiley':ashiley}
    return render(request, 'trucks/index.html',context)

def aboutpage(request):
    return render(request, 'trucks/about.html')









                
            
        
