from rest_framework.parsers import FormParser
from rest_framework import viewsets
from .models import UploadedFile
from .serializers import UploaderSerializer, ShowUploaderSerializer
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action, permission_classes
from django.shortcuts import get_object_or_404
import os


class UploaderViewSet(viewsets.ViewSet):
    """
    This class is just for show list and detail uploaded file.
    also users can uploade files or delete exited file.
    """
    serializer_class = UploaderSerializer 
    queryset = UploadedFile.objects.all()


    def list(self, request):
        user = self.request.user
        _queryset = UploadedFile.objects.filter(user=user)  
        serialize_data = ShowUploaderSerializer(_queryset, many=True)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        user = self.request.user
        _data = get_object_or_404(self.queryset, pk=pk, user=user)
        serialize_data = UploaderSerializer(_data)
        return Response(serialize_data.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        user = self.request.user
        instance = get_object_or_404(self.queryset, pk=pk, user=user)
        instance.delete()
        response = "successfully delete..."
        return Response(response, status=status.HTTP_204_NO_CONTENT)
       
    def create(self, request):
        file_uploaded = request.data
        file_serializer = UploaderSerializer(data=file_uploaded)
        file_path = request.data.get('file_path')
        file_size = file_path.size
        file_name, file_type = os.path.splitext(str(file_path))
        file_serializer = self.serializer_class(data=request.data, context={'user': request.user, 'file_size': file_size, 'file_type': file_type[1:]})
        
        if file_serializer.is_valid():
            file_serializer.save()
            response = "successfully uploade..."
            return Response(response, status=status.HTTP_201_CREATED)
        else:
            response = "bad..."
            return Response(response, status=status.HTTP_201_CREATED)   
