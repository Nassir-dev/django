from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .models import Trucks
from client_app.models import Client






# Create your views here.
def homepage(request):
    trucks = Trucks.objects.order_by('date_handled')
    ashiley = Trucks.objects.filter(client__name__iexact='ashiley').count()
    lutor = Trucks.objects.filter(client__name__iexact='lutor').count()
    daneva = Trucks.objects.filter(client__name__iexact='daneva').count()
    context = {'trucks':trucks, 
                'ashiley':ashiley,
                'lutor':lutor,
                'daneva':daneva}
    return render(request, 'trucks/index.html',context)

def aboutpage(request):
    return render(request, 'trucks/about.html')









                
            
        
