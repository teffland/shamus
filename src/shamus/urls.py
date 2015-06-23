"""shamus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
admin.autodiscover()

# add the admin site
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)), # admin site
]

# add in restaurant views (menu related stuff)
urlpatterns += patterns('restaurant.views',
    # Home page
    url(r'^$', 'home', name='home'),
    url(r'^/$', 'home', name='home'),
    url(r'^home/$', 'home', name='home'),
    # Menu
    url(r'^menu/(?P<menutype>.*)/$', 'view_menu', name='view_menu'),

    url(r'^(?P<url>.*/)$', 'static', name='static') # static page catchall

)

"""
# add in the static pages catchall (services, gifts, about)
urlpatterns += ('restaurant.views',
    url(r'^(?P<url>).*/$', 'static', name='static')
)
"""