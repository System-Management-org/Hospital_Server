from django.urls import path
from .views import *

urlpatterns = [
    path('', PatientList.as_view(), name='patients'),
    path('id=/<str:patient_id>/', PatientDetail.as_view(), name='patient_detail'),
    path('allergies/', AllergiesList.as_view(), name='allergies_list'),
    path('immunization/', ImmunizationList.as_view(), name='immunization_list'),
    path('vitals/', VitalsList.as_view(), name='vitals_list'),
    path('condition/', MedicalConditionList.as_view(), name='medical_condition_list'),
    path('medication/', MedicationList.as_view(), name='medication_list'),
    path('medication/<str:patient_id>/', MedicationDetail.as_view(), name='medication_detail'),
    path('hospitalization/', HospitalizationList.as_view(), name='hospitalization_list'),
]