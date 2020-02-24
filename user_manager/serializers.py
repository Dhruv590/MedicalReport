from rest_framework import serializers
from .models import CustomUserManager,CustomUser,Hostel,DoctorProfile,StudentProfile

class CustomuserManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUserManager
        fields = '__all__'

class CustomuserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'

class HostelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hostel
        fields = '__all__'

class DoctorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = DoctorProfile
        fields = '__all__'

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = '__all__'