from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Allergies)
admin.site.register(Immunization)
admin.site.register(Vitals)
admin.site.register(MedicalCondition)
admin.site.register(Medication)
admin.site.register(Hospitalization)