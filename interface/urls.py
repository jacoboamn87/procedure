from django.conf.urls import patterns, url
from interface.views import *


urlpatterns = patterns('',
    url(r'^procedures/$', ProcedureList.as_view()),
    url(r'^procedure/(?P<id>\d+)$', ProcedureDetail.as_view()),
    url(r'^procedure/update/(?P<id>\d+)$', ProcedureUpdate.as_view()),
    url(r'^procedure/delete/(?P<id>\d+)$', ProcedureDelete.as_view()),
    url(r'^procedure/$', ProcedureCreate.as_view()),
)
