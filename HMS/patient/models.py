from django.db import models
from staff.models import *

# Create your models here.
class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True) #generate based on number of patients previously registered
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender_options = (('male', 'Male'), ('female', 'Female'), ('other', 'Other'))
    gender = models.CharField(max_length=200, choices=gender_options)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    res_address = models.CharField(max_length=200)
    registrar = models.ForeignKey(Staff, max_length=200, null=True, blank=True, on_delete=models.SET_NULL) #make foreign key once we get staff model
    status_options = (
                        ("Checked In", "Checked In"),
                        ("Admitted", "Admitted"),
                        ("Under Observation", "Under Observation"),
                        ("Discharged", "Discharged"),
                        ("Transferred", "Transferred"),
                        ("Surgery", "Surgery"),
                        ("Recovery", "Recovery"),
                        ("Emergency", "Emergency"),
                        ("Outpatient", "Outpatient"),
                        ("Deceased", "Deceased"),
                    )
    insurance_options = (('National', 'National'),
                         ('Private', 'Private'),
                         ('None', 'None'))
    insurance_type = models.CharField(choices=insurance_options, default='None')
    insurance_id = models.CharField(max_length=250, default=None, blank=True, null=True)
    status = models.CharField(max_length=50, choices=status_options, default=None, blank=True, null=True) #added patient status
    #added allergies and Immunizations fields to patient
    allergies = models.ManyToManyField('conditions.Allergies', blank=True)
    immunizations = models.ManyToManyField('conditions.Immunization', blank=True)


    def __str__(self):
        return self.first_name + " " + self.last_name
    
