from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from  django.contrib.auth import get_user_model
User = get_user_model()

#create and update cloud provider login serializer

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password_hint', 'phone')
        model = User

class UserLoginSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

