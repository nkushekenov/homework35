from django import template
import datetime

register = template.Library()

@register.filter(name='multiply')
def multiply(value, arg):
    try:
        return value * arg
    except:
        return ''

@register.filter(name='divide')
def divide(value, arg):
    try:
        return value / arg
    except:
        return ''
    
        
@register.simple_tag   
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)

@register.simple_tag
def greet(name):
    """Простое приветствие"""
    return f"Привет, {name}!"

