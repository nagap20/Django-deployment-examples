
from django import template
#{% load my_templates %}

register = template.Library()
@register.filter(name='cut')

def cut(value,arg):

    """
    cuts out all values of 'arg' from the string
    """

    return value.replace(arg,'')

#register.filter('cut',cut)
