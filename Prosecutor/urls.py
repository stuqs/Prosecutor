from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *
from django.conf import settings


# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', main_with_filter),
                       url(r'^structure/$', tree_structure),
                       url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/(?P<division>.+?)/$', show_structure),
                       url(r'^structure/(?P<po>.+?)/(?P<department>.+?)/$', show_structure),
                       url(r'^structure/(?P<po>.+?)/$', show_structure),
                       url(r'^ajax/department/$', ajax_department),
                       url(r'^ajax/division/$', ajax_division),
                       url(r'^file/$', download_file),
                       )

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': './media/'}),
                            )