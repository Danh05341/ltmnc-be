
from django.contrib import admin
from django.urls import path
from . import controller
urlpatterns = [
    path('login/', controller.ReactView)
   
]
