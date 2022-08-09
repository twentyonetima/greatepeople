from django import template
from men.models import *

register = template.Library()


@register.inclusion_tag('men/tags/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        categories = Category.objects.all()
    else:
        categories = Category.objects.order_by(sort)

    return {'categories': categories, 'cat_selected': cat_selected}


@register.simple_tag(name='get_post')
def get_post(filter=None):
    if not filter:
        return Men.objects.all()
    else:
        return Men.objects.filter(cat_id=filter)
