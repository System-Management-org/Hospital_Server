from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Nurse)
admin.site.register(Pharmacist)
admin.site.register(Cashier)
admin.site.register(Patient)
admin.site.register(Staff)
