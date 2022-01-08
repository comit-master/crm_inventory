
import django_filters
from .models import Order


class OrderFilter(django_filters.FilterSet): #class allows to link filter to order
    class Meta:
        model= Order
        fields='__all__'
        exclude=['date_creation', 'customer']