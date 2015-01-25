from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *


# admin.autodiscover()




urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main_page),

)
