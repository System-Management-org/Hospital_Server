from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Staff)
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(LabTechnician)
admin.site.register(Pharmacist)
admin.site.register(FrontDeskExecutive)
admin.site.register(Cashier)