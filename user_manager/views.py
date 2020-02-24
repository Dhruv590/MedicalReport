

from rest_framework import viewsets
from . import models
from . import serializers

class CustomUserManagerViewset(viewsets.ModelViewSet):
    queryset = models.CustomUserManager.objects.all()
    serializer_class = serializers.CustomuserManagerSerializer

class CustomUserViewset(viewsets.ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomuserSerializer

class HostelViewset(viewsets.ModelViewSet):
    queryset = models.Hostel.objects.all()
    serializer_class = serializers.HostelSerializer

class DoctorProfileViewset(viewsets.ModelViewSet):
    queryset = models.DoctorProfile.objects.all()
    serializer_class = serializers.DoctorProfileSerializer

class StudentProfileViewset(viewsets.ModelViewSet):
    queryset = models.StudentProfile.objects.all()
    serializer_class = serializers.StudentProfileSerializer