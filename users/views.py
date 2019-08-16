from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.

def signup_view(request):

    if request.method == 'POST':

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            #log the user
            return redirect('#')
    else:
            form = UserCreationForm()

    ##context = {'form':form}
    return render(request,'users/register.html', {'form':form})

def login_view(request):

    if request.method == 'POST':
        form = AuthenticationForm()

    else:
            form = AuthenticationForm(request.POST)
    return render(request,'users/login.html', {'form':form})
