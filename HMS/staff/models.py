from django.db import models

# Create your models here.

class FrontDeskExecutive(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200, null = True, blank = True)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Doctor(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   
    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class Nurse(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   
    def __str__(self):
        return self.first_name + " " + self.last_name

class LabTechnician(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   
    def __str__(self):
        return self.first_name + " " + self.last_name

class Pharmacist(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)
   
    def __str__(self):
        return self.first_name + " " + self.last_name


class Cashier(models.Model):
    staff_id = models.BigAutoField(primary_key=True, max_length=10)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    speciality = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name
    

class Staff(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    lab_technician = models.ForeignKey(LabTechnician, on_delete=models.CASCADE)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    cashier = models.ForeignKey(Cashier, on_delete=models.CASCADE)
    front_desk_executive = models.ForeignKey(FrontDeskExecutive, on_delete=models.CASCADE)

    def __str__(self):
        return self.doctor.first_name | self.nurse.first_name | self.lab_technician.first_name | self.pharmacist.first_name | self.cashier.first_name | self.front_desk_executive.first_name
