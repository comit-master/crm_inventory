"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationPage, name='registration'),
    path('login/', views.LoginPage, name='login'),

]