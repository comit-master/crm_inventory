from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from order.forms import OrderForm


def order_list(request):
    return render(request, 'order/order_list.html')

def add_order(request):
    form= OrderForm()
    if request.method=='POST':
        form= OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context={'order_form':form}
    return render(request, 'order/order_add.html', context)

