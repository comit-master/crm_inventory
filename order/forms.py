from django.forms import ModelForm
from .models import Order


class OrderForm(ModelForm): # class allows to link form to order
    class Meta:
        model=Order
        fields= '__all__'

