from django.urls import path
from .views import StudentList, StudentDetails

urlpatterns = [
    path('', StudentList.as_view()),
    path('<int:pk>', StudentDetails.as_view()),
]