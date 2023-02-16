from django.shortcuts import render

from .models import Student
from rest_framework.generics import ListCreateAPIView,  RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer

# Create your views here.
class StudentList(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetails(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer