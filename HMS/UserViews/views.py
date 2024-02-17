from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
#make api calls to the backend
#include registration which is done by admins
#send email to patient to confirm registration

class DoctorList(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DoctorDetail(APIView):
    def get_object(self, staff_id):
        try:
            return Doctor.objects.get(staff_id=staff_id)
        except Doctor.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, staff_id):
        doctor = self.get_object(staff_id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def put(self, request, staff_id):
        doctor = self.get_object(staff_id)
        serializer = DoctorSerializer(doctor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, staff_id):
        doctor = self.get_object(staff_id)
        doctor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class NurseList(APIView):
    def get(self, request):
        nurses = Nurse.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class NurseDetail(APIView):
    def get_object(self, staff_id):
        try:
            return Nurse.objects.get(staff_id=staff_id)
        except Nurse.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, staff_id):
        nurse = self.get_object(staff_id)
        serializer = NurseSerializer(nurse)
        return Response(serializer.data)
    
    def put(self, request, staff_id):
        nurse = self.get_object(staff_id)
        serializer = NurseSerializer(nurse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, staff_id):
        nurse = self.get_object(staff_id)
        nurse.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PharmacistList(APIView):
    def get(self, request):
        pharmacists = Pharmacist.objects.all()
        serializer = PharmacistSerializer(pharmacists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PharmacistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class PharmacistDetail(APIView):
    def get_object(self, staff_id):
        try:
            return Pharmacist.objects.get(staff_id=staff_id)
        except Pharmacist.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, staff_id):
        pharmacist = self.get_object(staff_id)
        serializer = PharmacistSerializer(pharmacist)
        return Response(serializer.data)
    
    def put(self, request, staff_id):
        pharmacist = self.get_object(staff_id)
        serializer = PharmacistSerializer(pharmacist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, staff_id):
        pharmacist = self.get_object(staff_id)
        pharmacist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CashierList(APIView):
    def get(self, request):
        cashiers = Cashier.objects.all()
        serializer = CashierSerializer(cashiers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CashierSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class CashierDetail(APIView):
    def get_object(self, staff_id):
        try:
            return Cashier.objects.get(staff_id=staff_id)
        except Cashier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, staff_id):
        cashier = self.get_object(staff_id)
        serializer = CashierSerializer(cashier)
        return Response(serializer.data)
    
    def put(self, request, staff_id):
        cashier = self.get_object(staff_id)
        serializer = CashierSerializer(cashier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, staff_id):
        cashier = self.get_object(staff_id)
        cashier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        current_user = request.user

        request_data = request.data.copy()
        request_data['registrar'] = current_user.id
        serializer = PatientSerializer(data=request_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetail(APIView):
    def get_object(self, patient_id):
        try:
            return Patient.objects.get(patient_id=patient_id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, patient_id):
        patient = self.get_object(patient_id)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, patient_id):
        patient = self.get_object(patient_id)
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, patient_id):
        patient = self.get_object(patient_id)
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class staffList(APIView):
    def get(self, request):
        staff = staff.objects.all()
        serializer = staffSerializer(staff, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = staffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)