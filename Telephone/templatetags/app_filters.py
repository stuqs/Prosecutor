from django.template import Variable, VariableDoesNotExist
from django import template


register = template.Library()


@register.filter(name='tel_get')
def tel_get(d, key):
    return d.get(key, '')
