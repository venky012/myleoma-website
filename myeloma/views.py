from django.shortcuts import render
from os import path
import shutil, os 
from django.conf import settings
from BTP.settings import MEDIA_DIR, MEDIA_ROOT
# from django.http import HttpResponse

# def home(req):
#     return render(req, 'Home.html')



from .forms import UploadForm
import shutil


def image_upload_view(request):
    """Process images uploaded by users"""
    # output_folder = os.mkdir(MEDIA_ROOT + '/folder-2')
    # output_folder = MEDIA_ROOT + '/folder-2'
    
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            # if path.exists("img_obj.image"):
            #     src = path.realpath("img_obj.image")
            #     shutil.copy2(src , output_folder)  'output_folder': output_folder, 'flag': True
            context =  {'form': form, 'img_obj': img_obj }
            return render(request, 'Home.html',context)
    else:
        form = UploadForm()
    return render(request, 'Home.html', {'form': form})
# Create your views here.


def index(request):
    dir = MEDIA_ROOT + '/folder-2'
    output_folder = os.mkdir(dir)
    if request.method == 'POST':
        form = UploadForm(request.FILES)
        if form.is_valid():
            form.save()
            img_obj_1 = form.instance
            if path.exists("img_obj_1.image"):
                src = path.realpath("img_obj.image")
                shutil.copy2(src , output_folder)
                context =  {'form': form, 'img_obj_1': img_obj_1 }
                return render(request, 'Home.html',context)
        else:
            form = UploadForm()
        return render(request, 'Home.html', {'form': form})
    
    # path = settings.MEDIA_ROOT
    # form = FolderForm(request.POST, request.FILES)
    # img_obj1 = form.instance
    # img_folder = os.mkdir(MEDIA_ROOT + '/folder-2')
    # context = {'form': form, 'img_folder': img_folder, 'img_obj1': img_obj1}
    # return render(request, "Home.html", context)

# def image_upload_new_folder_view(request):
#     """Process images uploaded by users"""
#     if request.method == 'POST':
#         form = FolderForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # Get the current instance object to display in the template
#             img_obj1 = form.instance
#             return render(request, 'Home.html', {'form': form, 'img_obj': img_obj1})
#     else:
#         form = UploadForm()
#     return render(request, 'Home.html', {'form': form})


# def process_view(request):
#     form = UploadForm(request.POST, request.FILES)
#     img_obj = form.instance
#     dirname = os.path.join(MEDIA_DIR, '/folder-2')  
#     os.mkdir(dirname)
#     shutil.copy(img_obj, dirname)
#     return render(request, 'Home.html', {'form': form, 'dirname': dirname})



# src = 'img_obj.image.url'
# dest = 'MEDIA_ROOT'

    # return render(request, 'Home.html', src)