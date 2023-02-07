from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'DELETE','POST'])
def student(request):
    if request.method == 'GET':
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = StudentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BADb_REQUEST)

    elif request.method == "DELETE":
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#     elif request.method == 'POST':
#         serializer = StudentSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def student_api(request, pk):
    # try:
    #     stu = Student.objects.get(pk=pk)
    # except student_api.DoesNotExit:
    #     return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        stu = Student.objects.get(pk=pk)
        # print(">>>>>>>>>>>>>>>>>",stu)
        serializer = StudentSerializers(stu)
        return Response(serializer.data)


    elif request.method == "PUT":
        stu = Student.objects.get(pk=pk)
        serializer = StudentSerializers(stu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
