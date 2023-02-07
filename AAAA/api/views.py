from django.shortcuts import render
from .models import TestCamp
from .serializers import TestCampSerializer
from rest_framework import viewsets

# Create your views here.
class TestCampViewSet(viewsets.ModelViewSet):
    queryset = TestCamp.objects.all()
    serializer_class = TestCampSerializer
    