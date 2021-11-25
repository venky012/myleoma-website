from django.db import models

# Create your models here.
class UploadImage(models.Model):  
    image = models.ImageField(upload_to='folder-1/')  
    

# class new_folder(models.Model):
#     image = models.ImageField(upload_to='folder-2/')
#     def __str__(self):  
#         return self.caption  