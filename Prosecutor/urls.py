from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *


# admin.autodiscover()




urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Prosecutor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),


    # url(r'^contact/$', contacts.contact),
    # url(r'^contact/thanks/$', contacts.thanks),
)
