from django import template

register = template.Library()

@register.filter
def is_editor(user):
    """ Checks if user is an editor """
    return user.groups.filter(name='Editor').exists()

@register.filter
def is_author(user):
    """ Checks if user is an editor """
    return user.groups.filter(name='Autor').exists()

@register.filter
def has_group(user, group_name):
    """ Checks if user is an editor """
    return user.groups.filter(name=group_name).exists()
