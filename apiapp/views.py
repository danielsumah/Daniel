# from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse

# # Create your views here.

# def home(request):
#     data = {
#         'message': 'This is a json response'
#     }

#     return JsonResponse(data)

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializers

class CreateStudentViews(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class ReadStudentViews(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class UpdateStudentViews(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    
class DeleteStudentViews(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

