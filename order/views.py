from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def order_list(request):
    return HttpResponse('order list here')
