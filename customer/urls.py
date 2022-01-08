"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views

urlpatterns = [
    path('/<str:pk>', views.customer_list, name='customer' ), #string creation id on url after insert id on tag from html


]