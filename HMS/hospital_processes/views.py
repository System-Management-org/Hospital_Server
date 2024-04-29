from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CheckInSerializer, AppointmentSerializer, DiagnosticTestsSerializer
from .models import *

# Create your views here.

class CheckInList(APIView):
    def get(self, request):
        checked_in = CheckIn.objects.all()
        serializer = CheckInSerializer(checked_in, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CheckInSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class AppointmentsList(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            
            #add logic to send email to patient
            #send_appointment_email(request.data['email'], request.data['appointment_date'], request.data['staff'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class DiagnosticTestsList(APIView):
    def get(self, request):
        diagnostic_tests = DiagnosticTests.objects.all()
        serializer = DiagnosticTestsSerializer(diagnostic_tests, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = DiagnosticTestsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    