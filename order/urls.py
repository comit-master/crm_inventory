"""project URL Configuration

config url product == home page
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.order_list ),
    path('add_order/', views.add_order, name='add_order'),
    path('update_order/<str:pk>', views.update_order, name='modify_order'),
    path('delete_order/<str:pk>', views.delete_order, name='delete_order'),

]