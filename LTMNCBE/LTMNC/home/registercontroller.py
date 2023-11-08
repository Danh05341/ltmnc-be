from django.shortcuts import render
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
# Create your views here.

class ReactViewRegister(APIView):
	
	serializer_class = ReactSerializer
	def post(self, request):
		authen= 0
		
		try:
			p = User(email= request.data.get('email',''),password = request.data.get('password',''),id=User.objects.all().count()+1)
			p.save()
			authen=1
		except :
			authen = 0
		return Response(authen)
		
