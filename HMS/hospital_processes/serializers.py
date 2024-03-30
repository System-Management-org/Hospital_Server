from rest_framework import serializers
from .models import *

class CheckInSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckIn
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

class DiagnosticTestsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTests
        fields = '__all__'

class SurgeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgeries
        fields = '__all__'

class MedicalNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNotes
        fields = '__all__'