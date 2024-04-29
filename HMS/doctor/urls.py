from django.urls import path
from .views import *

urlpatterns = [
    path('surgeries/', SurgeriesList.as_view(), name='surgeries_list'),
    path('notes/', MedicalNotesList.as_view(), name='medical_notes_list')
]