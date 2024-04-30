from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.http import Http404
from staff.models import *

# Create your views here.

class UserRegistration(APIView):
    # permission_classes = [IsAuthenticated]

    # def get(self, request):
    #     # Access the current user
    #     current_user = request.user

    #     # Now you can use the current_user object as needed
    #     user_data = {
    #         'username': current_user.username,
    #         # Add more fields as needed
    #     }
    
    #     return Response(user_data)
    def get_object(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            raise Http404("User does not exist")
        
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            staff_id = request.data['staff_id']
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            birthdate = request.data['birthdate']
            email = request.data['email']
            phone = request.data['phone']
            speciality = request.data['speciality']
            role = request.data['role']

            #check if user already exists
            if self.get_object(email):
                return Response("User already exists", status=status.HTTP_400_BAD_REQUEST)
            #check if user is a doctor
            if role == 'Doctor':
                doctor = Doctor.objects.create(staff_id = staff_id, first_name = first_name, last_name = last_name, birthdate = birthdate, email = email, phone = phone, speciality = speciality)
                serializer.save(Doctor = doctor)
            #check if user is a nurse
            elif role == 'Nurse':
                nurse = Nurse.objects.create(staff_id = staff_id, first_name = first_name, last_name = last_name, birthdate = birthdate, email = email, phone = phone, speciality = speciality)
                serializer.save(Nurse = nurse)
            #check if user is a pharmacist
            elif role == 'Pharmacist':
                pharmacist = Pharmacist.objects.create(staff_id = staff_id, first_name = first_name, last_name = last_name, birthdate = birthdate, email = email, phone = phone, speciality = speciality)
                serializer.save(Pharmacist = pharmacist)
            #check if user is a cashier
            elif role == 'Cashier':
                cashier = Cashier.objects.create(staff_id = staff_id, first_name = first_name, last_name = last_name, birthdate = birthdate, email = email, phone = phone, speciality = speciality)
                serializer.save(Cashier = cashier)
            #check if user is a front desk executive
            elif role == 'Front Desk Executive':
                front_desk = FrontDeskExecutive.objects.create(staff_id = staff_id, first_name = first_name, last_name = last_name, birthdate = birthdate, email = email, phone = phone, speciality = speciality)
                serializer.save(Front_Desk = front_desk)
            else:
                return Response("Invalid role", status=status.HTTP_400_BAD_REQUEST)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  #add changing password endpoint in new app called "general"
    def put(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            user = self.get_object(request.data['email'])
            #new password not equal to oldpassword and equal to confirm password
            if request.data['new_password'] == request.data['confirm_password'] and request.data['new_password'] != user.password:
                user.password = request.data['new_password']
                user.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #delete a user
    def delete(self, request):
        user = self.get_object(request.data['email'])
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)