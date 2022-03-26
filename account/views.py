from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def RegistrationPage(request):
    form= CreateUser()
    if request.method=='POST':
        form= CreateUser(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Account created with success ' + user)
            return redirect('login')
    context={'form':form}
    return render(request, 'account/registration.html', context)

def LoginPage(request):
    form= CreateUser()
    if request.method=='POST':
        username= request.POST.get('username')
        password=request.POST.get('password')
        user= authenticate(request, username=username, password=password) #verifie si cohérence entre l'input de
        # l'user et ce qu'il ya dans la base de données
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'User and/or password not valid')
    return render(request, 'account/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')
