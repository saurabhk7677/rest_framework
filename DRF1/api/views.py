from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# DRF Read Operation.
@csrf_exempt
# def student_api(request):
#     if request.method == "GET": 
#         json_data = request.body
#         stream = io.BytesIO(json_data)
#         pythondata = JSONParser().parse(stream)
#         id = pythondata.get('id', None)
#         if id is not None:
#             stu = Student.objects.get(id=id)
#             serializers = StudentSerializers(stu)
#             json_data = JSONRenderer().render(serializers.data)
#             return HttpResponse(json_data, content_type='application/json')

#         stu = Student.objects.all()
#         serializers = StudentSerializers(stu, many=True)
#         return JsonResponse(serializers.data, content_type='application/json', safe=False)

def student_api(request):
    if request.method == "GET":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id', None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')
        
        stu = Student.objects.all()
        serializer = StudentSerializers(stu, many=True)
        return JsonResponse(serializer.data, content_type='application/json', safe=False)





    # if request.method == "POST":
    #     json_data = request.body
    #     stream = io.BytesIO(json_data)
    #     pythondata = JSONParser().parse(stream)
    #     serializer = StudentSerializers(data=pythondata)
    #     if serializer.is_valid():
    #         serializer.save()
    #         res = {'msg': 'Data Created!'}
    #         json_data = JSONRenderer().render(res)
    #         return HttpResponse(json_data, content_type='application/json')

    #     json_data = JSONRenderer().render(serializers.errors)
    #     return HttpResponse(json_data, content_type='application/json')