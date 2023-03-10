from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    # filterset_fields = ['city']   <----------------if you can user for global settings.py-------------------->
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'name']