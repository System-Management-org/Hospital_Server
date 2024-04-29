from rest_framework import serializers
from .models import *

class SurgeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surgeries
        fields = '__all__'

class MedicalNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalNotes
        fields = '__all__'