from django.db import models
from user_manager.models import *


# Create your models here.
class Visit(models.Model):
    patient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='patient_visit_user')
    date = models.DateField()
    location = models.CharField(max_length=100)
    purpose = models.CharField(max_length=250)

    def __str__(self):
        return str(self.patient)+"-"+str(self.date)+"-"+str(self.location)

class Examination(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    RS_CHOICES = (
        ('1', 'RHONCHI'),
        ('2', 'CREEPS'),
        ('3', 'AIR ENTRY'),
        ('4', 'OTHER'),
    )
    RS = models.CharField(max_length=100, choices=RS_CHOICES)
    RS_comments = models.CharField(max_length=250, null=True, blank=True)

    CVC_CHOICES = (
        ('1', 'HR'),
        ('2', 'OTHER'),
    )
    CVC = models.CharField(max_length=100, choices=CVC_CHOICES)
    CVC_comments = models.CharField(max_length=250, null=True, blank=True)

    ABD_CHOICES = (
        ('1', 'LIVER'),
        ('2', 'SPLEEN'),
        ('3', 'STOMCH'),
        ('4', 'INTESTINE'),
        ('5', 'KIDENY'),
        ('6', 'UTERINE'),
        ('7', 'GENITLE'),
        ('8', 'OTHER'),
    )
    ABD = models.CharField(max_length=100, choices=ABD_CHOICES)
    ABD_comments = models.CharField(max_length=250, null=True, blank=True)
    CNS_CHOICES = (
        ('1', 'SENSORY'),
        ('2', 'MOTOR'),
        ('3', 'OTHER'),
    )
    CNS = models.CharField(max_length=100, choices=CNS_CHOICES)
    CNS_comments = models.CharField(max_length=250, null=True, blank=True)
    SKIN_CHOICES = (
        ('1', 'COLOUR'),
        ('2', 'ERUPTION'),
        ('3', 'OTHER'),
    )
    SKIN = models.CharField(max_length=100, choices=SKIN_CHOICES)
    SKIN_comments = models.CharField(max_length=250, null=True, blank=True)

    GENREAL_comments = models.CharField(max_length=250)
    HEAD_comments = models.CharField(max_length=250)
    EXTRIMTY_comments = models.CharField(max_length=250)

    def __str__(self):
        return str(self.visit)

class Diagnosis(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    provisional = models.CharField(max_length=250)
    final = models.CharField(max_length=250)

    def __str__(self):
        return str(self.visit)


class MedicalReport(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    REPORT_CHOICES = (
        ('1', 'Blood'),
        ('2', 'Urine'),
        ('3', 'X-Ray'),
        ('4', 'MRI'),
        ('5', 'CT scan'),
        ('6', 'Biopsy'),
        ('7', 'None')
    )

    medical_report = models.CharField(max_length=100, choices=REPORT_CHOICES)
    comments = models.CharField(max_length=250)

    def __str__(self):
        return str(self.visit)

class Treatment(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    medicine = models.CharField(max_length=250, null=True, blank=True)
    notes = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.visit)


