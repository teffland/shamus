from django import template
from restaurant.models import MenuType

register = template.Library()

@register.assignment_tag
def menu_types():
    return MenuType.objects.all().order_by('start_time')

