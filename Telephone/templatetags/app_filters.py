from django.template import Variable, VariableDoesNotExist
from django import template


register = template.Library()


@register.filter(name='tel_get')
def tel_get(d, key):
    """
    Custom template filter, for getting dict values  from keys
    """
    return d.get(key, '')
