from django.db import models
from django.contrib.auth import get_user_model


User=get_user_model()


class UploadedFile(models.Model):
    """
    This is just for uploaded user files
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='files')
    file_path = models.FileField(upload_to="files/", blank=False, null=False)
    file_type = models.CharField(max_length=50)
    file_size = models.IntegerField(default=0)

   
    def __str__(self):
        return f'{self.user} - {str(self.file_path.name)} - {self.file_size}'

    def delete(self, *args, **kwargs):
        """
        Delete must be overridden because the inherited delete method does not call self.file.delete().
        """
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)

