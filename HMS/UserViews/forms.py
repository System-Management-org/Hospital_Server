from django import forms
from .models import *

class PatientForm(forms.ModelForm):
    patient_id = models.CharField(max_length=200) #generate based on number of patients previously registered
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateField()
    gender = forms.ChoiceField(widget=forms.RadioSelect(choices=Patient.GENDER_CHOICES), help_text="Gender")
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    res_address = models.CharField(max_length=200)
    registrar = models.CharField(max_length=200)

    class Meta:
        model = Patient
        fields = '__all__'