from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser

# Create your views here.
def RegistrationPage(request):
    form= CreateUser(request.POST)
    context={'form':form}
    return render(request, 'account/registration.html', context)

def LoginPage(request):
    context={}
    return render(request, 'account/login.html', context)

