from django.shortcuts import render
from django.Http import HttpResponse

# Create your views here.


def indexview(request):
    return HttpResponse("Hello this is the Index page")
