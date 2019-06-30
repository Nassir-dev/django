from django.shortcuts import render
from django.http import HttpResponse





# Create your views here.


def indexview(request):
    return render(request,'trucks/begin.html')

def homepage(request):
    return render(request, 'trucks/index.html')

def aboutpage(request):
    return render(request, 'trucks/about.html')


def contactme(request):
    return render(request, 'trucks/contact.html')

def accounts(request):
    return render(request, 'trucks/accounts.html')


                
            
        
    

