from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('singerapi/', views.SingerViewSet, basename='singerapi'),
router.register('songapi/', views.SongViewSet, basename='songapi')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
