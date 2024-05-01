from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import *

from .models import *

# Create your views here.

class AllergiesList(APIView):
    def get(self, request):
        allergies = Allergies.objects.all()
        serializer = AllergiesSerializer(allergies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AllergiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class ImmunizationList(APIView):
    def get(self, request):
        immunizations = Immunization.objects.all()
        serializer = ImmunizationSerializer(immunizations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ImmunizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class VitalsList(APIView):
    def get(self, request):
        vitals = Vitals.objects.all()
        serializer = VitalsSerializer(vitals, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VitalsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class MedicalConditionList(APIView):
    def get(self, request):
        medical_conditions = MedicalCondition.objects.all()
        serializer = MedicalConditionSerializer(medical_conditions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicalConditionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class MedicationList(APIView):
    def get(self, request):
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class MedicationDetail(APIView):
    def get_object(self, patient_id):
        try:
            return Medication.objects.get(patient_id= patient_id)
        except Medication.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        medication = self.get_object(request.data["patient_id"])
        serializer = MedicationSerializer(medication)
        return Response(serializer.data)
    
    def put(self, request):
        medication = self.get_object(request.data["patient_id"])
        serializer = MedicationSerializer(medication, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        medication = self.get_object(request.data["patient_id"])
        medication.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class HospitalizationList(APIView):
    def get(self, request):
        hospitalizations = Hospitalization.objects.all()
        serializer = HospitalizationSerializer(hospitalizations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = HospitalizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)