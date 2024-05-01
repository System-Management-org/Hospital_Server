from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import PatientSerializer
from .models import Patient
from django.http import Http404

# Create your views here.

class PatientList(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PatientSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PatientDetail(APIView):
    def get_object(self, patient_id):
        try:
            return Patient.objects.get(patient_id= patient_id)
        except Patient.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request):
        patient = self.get_object(request.data["patient_id"])
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request):
        patient = self.get_object(request.data["patient_id"])
        serializer = PatientSerializer(patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):
        patient = self.get_object(request.data["patient_id"])
        #might need to add logic to delete all appointments and checkins
        patient.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


