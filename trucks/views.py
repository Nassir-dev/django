from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexview(request):
    return HttpResponse("Hello this is the Index page")

def homepage(request):
    return HttpResponse("this now home")

def aboutpage(request):
    return HttpResponse("this is the about page call me now")

def contactme(request):
    return HttpResponse("This is the contact us page")

def accounts(request):
    return HttpResponse("This will be the accounts page")
