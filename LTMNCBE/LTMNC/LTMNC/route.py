
from django.contrib import admin
from django.urls import path,include

from home.controller import *
from home.registercontroller import *
from home.uploadController import *
from home.img2pptController import *
from home.downloadController import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', ReactView.as_view(), name="login"),
     path('register', ReactViewRegister.as_view(), name="register"),
     path('upload', Upload.as_view(), name="register"),
     path('result', img2pptController.as_view(), name="register"),
      path('download', downloadController.as_view(), name="register"),
    
]
