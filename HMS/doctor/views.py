from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckInSerializer, AppointmentSerializer, DiagnosticTestsSerializer, SurgeriesSerializer, MedicalNotesSerializer
from .models import *

# Create your views here.


class SurgeriesList(APIView):
    def get(self, request):
        surgeries = Surgeries.objects.all()
        serializer = SurgeriesSerializer(surgeries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = SurgeriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class MedicalNotesList(APIView):
    def get(self, request):
        medical_notes = MedicalNotes.objects.all()
        serializer = MedicalNotesSerializer(medical_notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MedicalNotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)