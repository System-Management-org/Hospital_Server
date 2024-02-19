#seialization
from rest_framework import serializers

from HMS.serializers import UserSerializer
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Doctor
        fields = '__all__'


class PharmacistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacist
        fields = '__all__'


class NurseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nurse
        fields = '__all__'


class CashierSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cashier
        fields = '__all__'

class staffSerializer(serializers.ModelSerializer):
    
        class Meta:
            model = Staff
            fields = '__all__'
            
class CheckInSerializer(serializers.Serializer):

    class Meta:
        model = CheckIn
        fields = '__all__'


class AppointmentSerializer(serializers.Serializer):

    class Meta:
        fields = '__all__'
