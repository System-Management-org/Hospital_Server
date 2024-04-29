from django.urls import path
from .views import *

urlpatterns = [
    path('checkin/', CheckInList.as_view(), name='checkin_list'),
    path('appointments/', AppointmentsList.as_view(), name='appointments_list'),
    path('tests/', DiagnosticTestsList.as_view(), name='diagnostic_tests_list'),
]