from django.conf.urls.defaults import patterns, include, url
from crawlerprj.views import search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crawlerprj.views.home', name='home'),
    # url(r'^crawlerprj/', include('crawlerprj.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^search/$', search),
    url(r'^admin/', include(admin.site.urls)),
)
