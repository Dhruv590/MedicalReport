from rest_framework import serializers
from .models import *


class ReportBriefSerializer(serializers.ModelSerializer):
    visit_date = serializers.CharField(source='visit.date', read_only=True)
    student_name = serializers.CharField(source='visit.patient.get_full_name', read_only=True)

    class Meta:
        model = Report
        fields = (
            'id',
            'visit',
            'visit_date',
            'summary',
            'student_name'
        )


class ReportDetailSerializer(serializers.ModelSerializer):
    visit_date = serializers.CharField(source='visit.date', read_only=True)
    student_name = serializers.CharField(source='visit.patient.get_full_name', read_only=True)
    purpose = serializers.CharField(source='visit.purpose', read_only=True)

    class Meta:
        model = Report
        fields = (
            'id',
            'visit',
            'visit_date',
            'purpose',
            'summary',
            'student_name'
        )