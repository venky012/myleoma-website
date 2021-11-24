from django.urls import path  
from django.contrib import admin
from . import views
# from .views import image_request  
  
# app_name = 'sampleapp'  
urlpatterns = [  
    # path('', image_request, name = "image-request")  
    # path('admin/', admin.site.urls),
    path('', views.image_upload_view, name = 'home'),
    path('', views.index, name = "home"),
]


