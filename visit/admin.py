from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Visit)
admin.site.register(Examination)
admin.site.register(Diagnosis)
admin.site.register(MedicalReport)
admin.site.register(Treatment)
admin.site.register(Report)