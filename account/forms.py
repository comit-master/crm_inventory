from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUser(UserCreationForm): # class allows to display pre-registered form
    class Meta:
        model=User
        fields= ['username', 'email', 'password1', 'password2'] # fields added

