from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser

# Create your views here.
def RegistrationPage(request):
    form= CreateUser()
    if request.method=='POST':
        form= CreateUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context={'form':form}
    return render(request, 'account/registration.html', context)

def LoginPage(request):
    context={}
    return render(request, 'account/login.html', context)

