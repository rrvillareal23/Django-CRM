# custom_filters.py

from django import template

register = template.Library()

@register.filter
def toggle_sort_order(order):
    return 'desc' if order == 'asc' else 'asc'
