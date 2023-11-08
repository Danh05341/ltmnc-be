from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from . img2ppt import *
import cv2
import os
import shutil
class Upload(APIView):
	serializer_class = ReactSerializer
	def post(self, request):
		listImg = request.FILES.getlist('file')
		img_path=r"E:\Web\LTMNC\home\img"
		if not os.path.exists(img_path):
			os.makedirs(img_path)
		for image in listImg:
			name  = image.name
			save_path = r'E:\Web\LTMNC\home\img\{}'.format(name)
			with open(save_path, 'wb') as f:
				f.write(image.read())
		create_pptx(img_path=r"E:\Web\LTMNC\home\img",height=30.0,width=53.333)  
		path = 'E:\Web\LTMNC\home\img'
		shutil.rmtree(path)
		return Response()
		
