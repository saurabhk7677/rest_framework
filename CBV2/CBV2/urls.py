from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.student),
    path('stu/<int:pk>', views.student_api),
]
