from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """Умножает значение на аргумент"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def add(value, arg):
    """Складывает значение с аргументом"""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return value