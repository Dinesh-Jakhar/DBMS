# custom_filters.py

from django import template

register = template.Library()

@register.filter
def increment_by_10(value):
    return value + 10
