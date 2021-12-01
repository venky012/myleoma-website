from django.shortcuts import render
from os import path
import shutil, os 
from django.conf import settings
from BTP.settings import MEDIA_DIR, MEDIA_ROOT
# from django.http import HttpResponse

# def home(req):
#     return render(req, 'Home.html')


from .models import UploadImage
from .forms import UploadForm
import shutil
import cv2
import matplotlib.pyplot as plt
import os
import glob


def image_upload_view(request):
    
    # delete files
    path = MEDIA_DIR.replace('\\','/')
    try:
        print(os.path.exists(path))
        if os.path.exists(path):
            shutil.rmtree(path)
    finally:
        os.mkdir(path)
        os.mkdir(path+'folder-1')
        os.mkdir(path+'folder-2')

    # get files and do the processing
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            final = None

            ##############################################################
            
            # model operations
            # print(type(img_obj),img_obj.image)
            # print(cv2.imread(MEDIA_DIR+str(img_obj.image)))

            ##############################################################
            if img_obj.image:
                src = MEDIA_DIR + str(img_obj.image)
                final = "/media/" + str(img_obj.image).replace("folder-1","folder-2")
                shutil.copy2(src,  MEDIA_DIR + 'folder-2')
            context =  {'form': form, 'original': img_obj , 'predicted':final,'media_dir':MEDIA_DIR}
            return render(request, 'Home.html',context)
    else:
        form = UploadForm()
    return render(request, 'Home.html', {'form': form})


# def index(request):
#     dir = MEDIA_ROOT + '/folder-2'
#     output_folder = os.mkdir(dir)
#     if request.method == 'POST':
#         form = UploadForm(request.FILES)
#         if form.is_valid():
#             form.save()
#             img_obj_1 = form.instance
#             if path.exists("img_obj_1.image"):
#                 src = path.realpath("img_obj.image")
#                 shutil.copy2(src , output_folder)
#                 context =  {'form': form, 'img_obj_1': img_obj_1 }
#                 return render(request, 'Home.html',context)
#         else:
#             form = UploadForm()
#         return render(request, 'Home.html', {'form': form})