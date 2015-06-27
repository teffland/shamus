from django import template
from django.template.defaultfilters import stringfilter

from restaurant.models import MenuType

register = template.Library()

@register.assignment_tag
def menu_types():
    """ Return all of the MenuType Items for the navigation bar """
    return MenuType.objects.all().order_by('start_time')

@register.filter
@stringfilter
def english_ordinal(value):
    """ Take a numeric order and return it's English ordinal.
            eg, 1 -> first

        NOTE:Currently only goes to 20
    """
    ordinals = {"1":"first",
                "2":"second",
                "3":"third",
                "4":"fourth",
                "5":"fifth",
                "6":"sixth",
                "7":"seventh",
                "8":"eighth",
                "9":"ninth",
                "10":"tenth",
                "11":"eleventh",
                "12":"twelfth",
                "13":"thirteenth",
                "14":"fourteenth",
                "15":"fifthteenth",
                "16":"sixteenth",
                "17":"seventeenth",
                "18":"eighteenth",
                "19":"nineteenth",
                "20":"twentieth"
                }
    try: 
        return ordinals[value]
    except: 
        return "Error: Value not in 1-20"