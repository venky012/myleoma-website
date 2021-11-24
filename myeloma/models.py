from django.db import models

# Create your models here.
class UploadImage(models.Model):  
    caption = models.CharField(max_length=200)  
    image = models.ImageField(upload_to='folder-1/')  
    
    def __str__(self):  
        return self.caption  

# class new_folder(models.Model):
#     image = models.ImageField(upload_to='folder-2/')
#     def __str__(self):  
#         return self.caption  