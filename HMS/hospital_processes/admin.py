from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(CheckIn)
admin.site.register(Appointment)
admin.site.register(DiagnosticTests)
admin.site.register(Surgeries)
admin.site.register(MedicalNotes)