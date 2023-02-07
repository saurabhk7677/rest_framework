from rest_framework import serializers
from .models import Student


class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)