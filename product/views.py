from django.http import HttpResponse
from django.shortcuts import render
from order.models import Order
from customer.models import Customer


# Create your views here.
def home(request):
    orders= Order.objects.all()
    customers= Customer.objects.all()
    context={'orders':orders, 'customers':customers}
    # Dictionary : I create here my key which is equal to my value, an object which
    # was created previously in which I imported all the data of my selected app class
    return render(request, 'product/homepage.html', context)
    # Everything is like push with the template, but my template doesnt know where
    # to push this data To do that, I go in the template and use tags functions


