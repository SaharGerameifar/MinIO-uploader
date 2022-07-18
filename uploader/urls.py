from django.urls import path, include
from rest_framework import routers
from . import views

app_name = "uploader"

router = routers.DefaultRouter()
router.register('', views.UploaderViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    
]
