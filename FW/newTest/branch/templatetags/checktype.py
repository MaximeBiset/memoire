"""
filters for checking the type of objects and formfields

Usage:

{% if form|obj_type:'mycustomform' %}
  <form class="custom" action="">
{% else %}
  <form action="">
{% endif %}


{% if field|field_type:'checkboxinput' %}
  <label class="cb_label">{{ field }} {{ field.label }}</label>
{% else %}
  <label for="id_{{ field.name }}">{{ field.label }}</label> {{ field }}
{% endif %}

"""

from django import template
register = template.Library()

def check_type(obj, stype):
    try:
        t = obj.__class__.__name__
        return t.lower() == str(stype).lower()
    except:
        pass
    return False
register.filter('obj_type', check_type)

def print_type(obj):
    try:
        return obj.__class__.__name__
    except:
        pass
    return 'lol'

def field_type(field, ftype):
    return check_type(field.field.widget, ftype)
register.filter('field_type', field_type)
