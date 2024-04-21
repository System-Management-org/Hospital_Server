from django.db import models
from staff.models import Doctor, Staff
from patient.models import Patient, MedicalCondition
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