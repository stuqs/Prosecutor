from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *
from django.conf import settings


# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', main_with_filter),
                       url(r'^structure/$', tree_structure),
                       # url(r'^structure/(?P<po>.+?)/$', test_f),
                       # url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/$', test_f),
                       # url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/(?P<division>.+?)/$', test_f),
                       url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/(?P<division>.+?)/$', test_f),
                       url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/$', test_f),
                       url(r'^structure/(?P<po>.+?)/$', test_f),


                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
                            )