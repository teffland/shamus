from django.shortcuts import render, get_object_or_404, get_list_or_404

from restaurant.models import MenuItem, MenuType, MenuCategory, SliderImage, StaticPage, FrontPageBlurb
# Create your views here.
def home(request):
    context = {}
    imgs = SliderImage.objects.filter(published=True).order_by('order_affinity')
    context['imgs'] = imgs
    blurbs = FrontPageBlurb.objects.filter(published=True).order_by('order_affinity')
    context['blurbs'] = blurbs

    return render(request, 'home.html', context)

def view_menu(request, menutype):
    menutype= get_object_or_404(MenuType, name=menutype)
    categories = menutype.categories()

    context = { 'menutype': menutype,
                'categories': categories
                }
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