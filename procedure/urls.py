from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from procedure import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'step', views.StepViewSet)
router.register(r'procedure', views.ProcedureViewSet)
router.register(r'precedence', views.PrecedenceViewSet)
urlpatterns = router.urls

#urlpatterns = patterns('procedure.views',
#    url(r'^procedure/$', views.ProcedureDetail.as_view(), name='procedure_list'),
#    url(r'^procedure/(?P<pk>[0-9]+)/$', views.ProcedureDetail.as_view(), name='procedure_details'),
#)

#urlpatterns = format_suffix_patterns(urlpatterns)