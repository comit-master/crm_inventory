from django.db import models

# Create your models here.

class Order(models.Model):
    STATUS = (('en instance','en instance'),
              ('non livré','non livré'),
              ('livré','livré'))

    #customer= models.CharField(max_lenght=200, null=True)
    #product= models.FloatField(max_lenght=200, null=True)
    status= models.CharField(max_length=200, null=True, choices=STATUS)
    date_creation= models.DateTimeField(auto_now_add=True, null=True)


