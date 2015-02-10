from django.conf.urls import patterns, include, url
from django.contrib import admin
from Telephone.views import *
from django.conf import settings

# admin.autodiscover()

urlpatterns = patterns('',

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', main_page),
                       url(r'^t/$', main_with_filter),
                       # url(r'^t/$', TemplateView.as_view(template_name='main1.html'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root':'./media/'}),
                            )