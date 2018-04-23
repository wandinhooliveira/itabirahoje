from django import template

register = template.Library()

@register.filter
def negrito(value): # Only one argument.
    """Converts a string into"""
    value = value.replace('&lt;','<')
    value = value.replace('&gt;','>')
    return value