from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
from .utils import ok_response, error_response
from .models import User



# Create your views here.
class Registration(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    name = "registration"

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():
            username = request.data.get('username')
            email = request.data.get('email')
            first_name = request.data.get('first_name')
            last_name = request.data.get('last_name')
            phone = request.data.get('phone')
            password = request.data.get('password')

            if not User.objects.filter(username=username).exists():
                if len(password) in range(4, 8):
                    total = len(password) - len(password[-2:])
                    hint_password = ("*"*total+password[-2:])
                else:
                    total = len(password) - len(password[-4:])
                    hint_password = ("*"*total+password[-4:])

                user = User.objects.create(username=username, email=email, first_name=first_name, last_name=last_name, password_hint=hint_password, phone=phone)
                user.set_password(request.data.get('password'))
                user.save()
                
                if user:
                    data = {
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'phone': user.phone,
                        'password_hint': user.password_hint,
                    }
                    return Response(ok_response(data=data, message='user added successfully.'))
                return Response(error_response(status_code= status.HTTP_400_BAD_REQUEST, message='user not added.', error_details=username))
            else:
                return Response(error_response(status_code=status.HTTP_409_CONFICT, message='username already exit chose diferent username.', error_details=username))
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


