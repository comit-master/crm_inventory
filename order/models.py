from django.db import models
from customer.models import Customer
from product.models import Product


# Create your models here.

class Order(models.Model):
    STATUS = (('en instance','en instance'),
              ('non livré','non livré'),
              ('livré','livré'))

#here below we udpate relation
    # order is related to customer and product tank to ForeignKey function from models
    customer= models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product= models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    status= models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation= models.DateTimeField(auto_now_add=True, null=True)


