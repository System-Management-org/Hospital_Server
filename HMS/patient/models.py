from django.db import models
from staff.models import Doctor, Nurse, Pharmacist, Staff

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True) #generate based on number of patients previously registered
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender_options = (('Male', 'male'), ('Female', 'female'), ('Other', 'other'))
    gender = models.CharField(max_length=200, choices=gender_options)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    res_address = models.CharField(max_length=200)
    registrar = models.CharField(max_length=200, null=True, blank=True) #make foreign key once we get staff model

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Allergies(models.Model):
    allergy_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    allergen = models.CharField(max_length=200)
    severity_options = (('High', 'high'), ('Moderate','moderate'), ('Low','low'))
    severity = models.CharField(choices=severity_options, max_length=20)

class Immunization(models.Model):
    immunization_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE) #ensure necessary
    vaccine = models.CharField(max_length=200)
    admission_date = models.DateField()
    
    def __str__(self):
        return self.staff.doctor.staff_id + " " + self.vaccine

class Vitals(models.Model):
    vital_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nurse_id = models.ForeignKey(Nurse, on_delete=models.CASCADE) #ensure necessary
    date_recorded = models.DateField() #ensure necessary
    temperature = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    blood_pressure = models.CharField(max_length=200)

class MedicalCondition(models.Model):
    condition_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE) #ensure necessary
    date_recorded = models.DateField() #ensure necessary
    diagnosis = models.CharField(max_length=200)
    treatment = models.CharField(max_length=200)
    prescription = models.CharField(max_length=200)

class Medication(models.Model):
    medication_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE) #ensure necessary
    pharmacist_id = models.ForeignKey(Pharmacist, on_delete=models.CASCADE) #ensure necessary
    date_prescribed = models.DateField() #ensure necessary
    drug_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.CharField(max_length=200)

class Hospitalization(models.Model):
    hospitalization_id = models.BigAutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date = models.DateField()
    discharge_date = models.DateField()
    reason = models.CharField(max_length=200)
    ward = models.CharField(max_length=200) #room number
    bed = models.CharField(max_length=200) #bed number