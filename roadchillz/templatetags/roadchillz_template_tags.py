from django import template

register = template.Library()


@register.inclusion_tag('roadchillz/nav.html')
def nav(request, path):
    """
    Returns the nav items for the current path.
    """
    return {'path': path}

