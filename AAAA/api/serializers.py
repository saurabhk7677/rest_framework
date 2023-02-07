from rest_framework import serializers
from .models import TestCamp

class TestCampSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestCamp
        fields = '__all__'