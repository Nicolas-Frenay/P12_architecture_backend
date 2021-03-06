from django_filters import rest_framework as filters
from .models import *

class ContractFilter(filters.FilterSet):
    """
    Filters for ContractViewset
    """
    date_contains = filters.CharFilter(field_name='date_created',
                                       lookup_expr='icontains')

    class Meta:
        model = Contract
        fields = [
            'customer__email',
            'customer__last_name',
            'customer__company',
            'date_created',
            'amount',
            'sale_contact'
        ]


class EventFilter(filters.FilterSet):
    """
    Filters for EventViewset
    """
    date_contains = filters.CharFilter(field_name='event_date',
                                       lookup_expr='icontains')
    class Meta:
        model = Event
        fields = [
            'customer__email',
            'customer__last_name',
            'customer__company',
            'event_date',
            'support_contact'
        ]


class CustomerFilter(filters.FilterSet):
    """
    Filters for CustomerViewset
    """
    class Meta:
        model = Customer
        fields = [
            'email',
            'last_name',
            'company',
            'sale_contact'
        ]