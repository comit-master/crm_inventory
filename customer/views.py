
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def customer_list(request):
    return render(request, 'customer/client_list.html')
