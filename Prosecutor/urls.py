from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *
from django.views.generic.base import TemplateView

# admin.autodiscover()




urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),
    url(r'^t/$', TemplateView.as_view(template_name='main1.html'))
)
