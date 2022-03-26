"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.allProducts),
    path('product/<int:id>', views.getProduct),


]