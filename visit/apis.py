from django.db.models import F
from rest_framework import views, viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework import mixins, status
from .serializers import *
from .models import *


class ReportBriefViewSet(mixins.ListModelMixin,
                         mixins.RetrieveModelMixin,
                         viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ReportBriefSerializer
    queryset = Report.objects.all()

    def get_queryset(self):
        return self.queryset.filter(visit__patient=self.request.user)


class ReportDetailViewSet(mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = ReportDetailSerializer
    queryset = Report.objects.all()

    def get_queryset(self):
        return self.queryset.filter(visit__patient=self.request.user)
