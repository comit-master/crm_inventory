from django.http import HttpResponse
from django.shortcuts import render
from order.models import Order
from customer.models import Customer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from product import serializers



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


#api view
@api_view(['GET'])
def allProducts(request): 
    products = Product.objects.all() #retrieve all products
    serialization = ProductSerializer(products, many=True) #mchange format to json
    return Response(serialization.data)
#----------------------------------------------------------------------------------------
@api_view(['GET'])
def getProduct(request,id):#displayinthepaththebooknumber
    product = Product.objects.get(id=id) #retrieveproductid
    serializer = ProductSerializer(product)
    return Response(serializer.data)
#----------------------------------------------------------------------------------------
