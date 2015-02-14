from django import template

register = template.Library()


classes = {
    'er': 'list-group-item-danger',
    'co': 'list-group-item-success',
    'lo': 'list-group-item-warning'
}


@register.filter
def list_status_classes(value):
    return classes.get(value, '')