from django.shortcuts import render, get_object_or_404, get_list_or_404

from restaurant.models import MenuItem, MenuType, MenuCategory, SliderImage, StaticPage
# Create your views here.
def home(request):
    context = {}

    return render(request, 'home.html', context)

def view_menu(request, menutype):
    print 'memnutype:', menutype
    menutype= get_object_or_404(MenuType, name=menutype)
    context = {'menutype': menutype}
    return render(request, 'menu.html', context)

def static(request, url=None):
    context = {}
    print "Url passed by parse: %s" % str(url)
    page = get_object_or_404(StaticPage, pk=url)
    context['title'] = page.title
    context['content'] = page.content

    return render(request, page.template, context)




"""
def service(request, service="all"):
    context = {'service': service}

    return render(request, '404.html', context)

def gifts(request):
    context = {}

    return render(request, '404.html', context)

def about(request):
    context = {}

    return render(request, '404.html', context)
"""