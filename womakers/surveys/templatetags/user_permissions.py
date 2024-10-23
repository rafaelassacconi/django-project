from django import template

register = template.Library()

def is_editor(user):
    """ Checks if user is an editor """
    return user.groups.filter(name='Editor').exists()

def is_author(user):
    """ Checks if user is an editor """
    return user.groups.filter(name='Autor').exists()

register.filter("is_editor", is_editor)
register.filter("is_author", is_author)
