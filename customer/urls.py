"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_list ),


]