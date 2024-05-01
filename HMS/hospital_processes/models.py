from django.db import models
from conditions.models import *
from staff.models import Doctor, Staff
from patient.models import *
# Create your models here.

class CheckIn(models.Model):
    checkin_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    checkin_time = models.DateTimeField() #on appointment, enter this
    checkout_time = models.DateTimeField(null=True, blank=True)
    doctor_assigned = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True) #on appointment, enter this
    status = models.BooleanField(default=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) #make foreign key once we get staff model
    isappointment = models.BooleanField(default=False) #added to check if user has an appointment in the system
    
    def __str__(self):
        return  self.patient_id.first_name + " " + self.patient_id.last_name + " " + self.checkin_id + " (A)" if self.isappointment else self.patient_id.first_name + " " + self.patient_id.last_name + " " + self.checkin_id
    

class Appointment(models.Model):
    appointment_id = models.BigAutoField(primary_key=True)
    patient_id = models.CharField(max_length=8)
    appointment_time = models.DateTimeField()
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) #make foreign key once we get staff model also, make a case for multiple staff members
    status = models.BooleanField(default=False) #added to check if user has an appointment in

    def __str__(self):
        return self.patient_id + " " + self.appointment_time + " " + self.staff
    
class DiagnosticTests(models.Model):
    condition_id = models.ForeignKey(MedicalCondition, on_delete=models.CASCADE)
    test_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=200)
    test_date = models.DateField()
    test_results = models.CharField(max_length=200)
        
    def __str__(self):
        return self.patient_id.first_name + "(" + self.patient_id.patient_id + ")" + " " + self.test_name
    