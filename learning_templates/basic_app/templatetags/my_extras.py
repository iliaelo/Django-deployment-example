from xml.dom import registerDOMImplementation
from django import template

register = template.Library()

@register.filter(name='cut')

def cut(value,args):
    """
    
    This cuts out all values of args from the string!
    
    """

    return value.replace(args,'')

#register.filter('cut',cut)