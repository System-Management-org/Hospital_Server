from django.urls import path
from .views import *

urlpatterns = [
    path('doctors/', DoctorList.as_view(), name='doctor_list'),
    path('doctor/<str:staff_id>', DoctorDetail.as_view(), name='doctor_detail'),
    path('nurses/', NurseList.as_view(), name='nurse_list'),
    path('nurse/<str:staff_id>', NurseDetail.as_view(), name='nurse_detail'),
    path('pharmacists/', PharmacistList.as_view(), name='pharmacist_list'),
    path('pharmacist/<str:staff_id>', PharmacistDetail.as_view(), name='pharmacist_detail'),
    path('lab_technicians/', LabTechnicianList.as_view(), name='lab_technician_list'),
    path('lab_technician/<str:staff_id>', LabTechnicianDetail.as_view(), name='lab_technician_detail'),
    path('cashiers/', CashierList.as_view(), name='cashier_list'),
    path('cashier/<str:staff_id>', CashierDetail.as_view(), name='cashier_detail'),
    path('receptionists/', FrontDeskList.as_view(), name='receptionist_list'),   
    path('receptionist/<str:staff_id>', FrontDeskDetail.as_view(), name='receptionist_detail'),
]