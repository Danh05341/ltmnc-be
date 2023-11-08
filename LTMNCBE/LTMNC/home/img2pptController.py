from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from .img2ppt import *
import cv2
import shutil
class img2pptController(APIView):
	serializer_class = ReactSerializer
	def post(self, request):
		create_pptx(img_path=r"E:\Web\LTMNC\home\img",height=30.0,width=53.333)  
		path = 'E:\Web\LTMNC\home\img'
		shutil.rmtree(path)
		return Response()
		
