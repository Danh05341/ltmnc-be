from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
from .img2ppt import *
from django.http import HttpResponse, FileResponse
import os
class downloadController(APIView):
	serializer_class = ReactSerializer
	def get(self,request):
		print('a')
		with open(r'E:\Web\LTMNC\home\img.pptx', 'rb') as file_content:
			response = HttpResponse(file_content.read(),content_type='application/vnd.openxmlformats-officedocument.presentationml.presentation')
			response['Content-Disposition'] = f'attachment; filename=img.pptx'

		path = r'E:\Web\LTMNC\home\img.pptx'
		if os.path.isfile(path):
			os.remove(path)
		
		return response
		
