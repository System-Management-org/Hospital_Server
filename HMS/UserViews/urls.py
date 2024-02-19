from django.urls import path
from . import views



urlpatterns = [
    path('patient/', views.PatientList.as_view(), name="patient_list"),
    path('patient/<str:patient_id>/', views.PatientDetail.as_view(), name="patient_detail"),
    path('checkedin/', views.CheckInList.as_view(), name='check_in')
]