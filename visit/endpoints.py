from django.urls import include, path
from django.conf.urls import url
from .apis import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register('report/brief', ReportBriefViewSet, 'report_brief')
router.register('report/detail', ReportDetailViewSet, 'report_detail')

urlpatterns = [
    url("^visit/", include(router.urls)),
]