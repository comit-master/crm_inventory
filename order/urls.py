"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list ),
    path('add_order/', views.add_order, name='add_order'),

]