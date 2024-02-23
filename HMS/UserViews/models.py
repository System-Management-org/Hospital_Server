from django.db import models


# Create your models here.
class Doctor(models.Model):
    staff_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Nurse(models.Model):
    staff_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   

    def __str__(self):
        return self.first_name + " " + self.last_name

class Pharmacist(models.Model):
    staff_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   

    def __str__(self):
        return self.first_name + " " + self.last_name

class Cashier(models.Model):
    staff_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   

    def __str__(self):
        return self.first_name + " " + self.last_name
    
class Patient(models.Model):
    patient_id = models.CharField(max_length=200) #generate based on number of patients previously registered
    first_name = models.CharField(max_length=200)
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
    

    #look into foreign key for registrar co

class Staff(models.Model):
    staff_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    job_desc = models.CharField(max_length=200)
   

    def __str__(self):
        return self.first_name + " " + self.last_name
    
#changeable models

class CheckIn(models.Model):
    patient_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200) #make foreign key once we get position of patient model
    checkin_time = models.DateTimeField()
    checkout_time = models.DateTimeField(null=True, blank=True)
    staff = models.CharField(max_length=200) #make foreign key once we get staff model

    def __str__(self):
        return self.patient_id + " " + self.checkin_time + " " + self.registrar
    
class Appointment(models.Model):
    patient_id = models.CharField(max_length=10)
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200, null=True, blank=True) #make foreign key once we get position of patient model
    appointment_time = models.DateTimeField()
    staff = models.CharField(max_length=200) #make foreign key once we get staff model also, make a case for multiple staff members
    

    def __str__(self):
        return self.patient_id + " " + self.appointment_time + " " + self.staff