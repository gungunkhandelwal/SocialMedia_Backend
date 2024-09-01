from django.shortcuts import render
from django.http import HttpResponse
from . serializer import *
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser,FormParser

class PostApi(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request,*args,**kwargs):
        data=Post.objects.all().order_by('-created_at')
        print(data)
        serializer=PostSerializer(data,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    


