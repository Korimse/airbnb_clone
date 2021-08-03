from django import template

register = template.Library()


@register.filter(name="my_capitals")
def my_capitals(value):
    return value.capitalize()
