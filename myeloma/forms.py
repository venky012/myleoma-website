from django import forms
from .models import UploadImage


class UploadForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = UploadImage
        fields = ['caption', 'image']

# class FolderForm(forms.ModelForm):
#     """Form for the image model"""
#     class Meta:
#         model = new_folder
#         fields = ['image']