from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^api/', include('procedure.urls')),
    url(r'^interface/', include('interface.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
