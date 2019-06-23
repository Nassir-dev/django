from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def indexview(request):
    return HttpResponse("Hello this is the Index page")

def homepage(request):
    return HttpResponse("this now home")
