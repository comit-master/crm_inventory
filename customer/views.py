
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer_list(request, pk):
    customer= Customer.objects.get(id=pk) # get function retrieve id and initialise it as pk
    order= customer.order_set.all() #all function did'nt work, to access to my data, all
    # function needed specific object type, it allows me to retrieve finally to my data in my second table
    # first table works without all function, just with _set function but not the second table which retrieve
    # all data from customer as what he buys or the category
    order_total=order.count()
    context={'customer':customer, 'order':order, 'order_count':order_total} #pk is used after in url and id in tag from html
    return render(request, 'customer/client_list.html', context)

