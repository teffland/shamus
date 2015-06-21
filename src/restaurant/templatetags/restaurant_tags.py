from django import template
from restaurant.models import MenuType

register = template.Library()

@register.simple_tag
def menu_types():
    menus = MenuType.objects.all().order_by('start_time')
    print "Menus:", menus
    return "Menu" #menus
