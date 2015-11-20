# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from test3.views import *


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test3.views.home', name='home'),
    # url(r'^test3/', include('test3.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #url(r'^admin/', include(admin.site.urls)),
    (r'^search_by_author/$',showbooks),
    (r'^delete/$',deletebook),
    (r'^show_book/$',showbooks2),
    (r'^show_author_books/$',searchbook),
	B3change
    #(r'^medias/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)
