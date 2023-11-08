from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from . serializer import *
# Create your views here.

class ReactView(APIView):
	
	serializer_class = ReactSerializer
	def post(self, request):
		authen= 0
		for ac in User.objects.all():
			if request.data.get('email','') == ac.email:
				if request.data.get('password','') == ac.password:
					authen = 1
		if authen: 
			print("YES")
		else :
			print("NO")
		return Response(authen)
		
