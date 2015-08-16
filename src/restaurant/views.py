from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
# for contact mail
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

from restaurant.models import MenuItem, MenuType, MenuCategory, SliderImage, StaticPage, FrontPageBlurb, MaintenanceMode
# Create your views here.
def home(request):
    if MaintenanceMode.get_solo().maintenance:
        return render(request, 'maintenance.html', {})
    context = {}
    imgs = SliderImage.objects.filter(published=True).order_by('order_affinity')
    context['imgs'] = imgs
    blurbs = FrontPageBlurb.objects.filter(published=True).order_by('order_affinity')
    context['blurbs'] = blurbs

    return render(request, 'home.html', context)

def view_menu(request, menutype):
    if MaintenanceMode.get_solo().maintenance:
        return render(request, 'maintenance.html', {})
    menutype= get_object_or_404(MenuType, name=menutype)
    categories = menutype.categories()

    context = { 'menutype': menutype,
                'categories': categories
                }
    return render(request, 'menu.html', context)

def static(request, url=None):
    if MaintenanceMode.get_solo().maintenance:
        return render(request, 'maintenance.html', {})
    context = {}
    print "Url passed by parse: %s" % str(url)
    page = get_object_or_404(StaticPage, pk=url)
    context['title'] = page.title
    context['content'] = page.content

    return render(request, page.template, context)
    