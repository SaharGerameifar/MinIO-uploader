from rest_framework import serializers
from .models import UploadedFile


class UploaderSerializer(serializers.ModelSerializer):
    """
    This is just for uploaded file
    """
    def create(self, validated_data):
        if self.context['user']:
            user = self.context['user']
            
            validated_data['user'] = user

        if self.context['file_size']:
            file_size = self.context['file_size']
            
            validated_data['file_size'] = file_size  

        if self.context['file_type']:
            file_type = self.context['file_type']
            
            validated_data['file_type'] = file_type

        file_ = UploadedFile.objects.create(**validated_data)
        return file_

    class Meta:
        model = UploadedFile
        fields = ['file_path']


class ShowUploaderSerializer(serializers.ModelSerializer):
    """
    This is just for show info uploaded file for file owner 
    """
    user = serializers.SerializerMethodField("get_user", read_only=True)

    def get_user(self, obj):
        return {"email": obj.user.email,
                "username": obj.user.username,
                "first_name": obj.user.first_name,
                "last_name": obj.user.last_name }

    class Meta:
        model = UploadedFile
        fields = ['user', 'file_path', 'file_size', 'file_type']


