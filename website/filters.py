import django_filters

from .models import *

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Record
        fields = [
            'id', 
            'email', 
            'project_status',
            'project_tier']