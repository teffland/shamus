from django.shortcuts import render, get_object_or_404, get_list_or_404
# for contact mail
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse

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

# def contact_us(request):
#     """ Contact form: code credit goes to http://code.runnable.com/Up-GkBztEBBIAAKo/making-a-contact-form-in-django-for-python"""
#     errors = []
#     if request.method == 'POST':
#         if not request.POST.get('subject', ''):
#             errors.append('Please enter a subject.')
#         if not request.POST.get('message', ''):
#             errors.append('Please enter a message.')
#         if request.POST.get('email') and '@' not in request.POST['email']:
#             errors.append('Please enter a valid e-mail address.')
#         if not errors:
#           try:
#             send_mail(
#                 request.POST['subject'],
#                 request.POST['message'],
#                 request.POST['email'], 
#                 ['tom.effland@gmail.com']
#             )
#             return render(request, 'basic_message.html', {'message':'Thank you, your email has been submitted successfully'})
#           except Exception, err: 
#             return render(request, 'basic_message.html', 
#                 {'message':"""Unfortunately the email was unable to send. 
#                 Please try again.  If the problem persists, please contact <a href="mailto:tom.effland@gmail.com"> the developer</a>.

#                 Please paste the following error code in your message to the developer:
#                 """+str(err)})

    return render(request, 'contact_form.html',
        {'errors': errors})

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