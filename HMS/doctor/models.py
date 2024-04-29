from django.db import models

from patient.models import *

# Create your models here.

class Surgeries(models.Model):
    condition_id = models.ForeignKey(MedicalCondition, on_delete=models.CASCADE)
    surgery_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    surgery_name = models.CharField(max_length=200)
    surgery_date = models.DateField()
    surgeon = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.patient_id.first_name + "(" + self.patient_id.patient_id + ")" + " " + self.surgery_name 
    


class MedicalNotes(models.Model):
    note_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    note_date = models.DateField()
    note = models.TextField()
    
    def __str__(self):
        return self.doctor_id.first_name + "(" + self.doctor_id.patient_id + ")"