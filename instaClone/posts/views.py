from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . serializer import *
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser

class PostListCreateApi(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request,*args,**kwargs):
        data=Post.objects.all().order_by('-created_at')
        serializer=PostSerializer(data,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)
    
    # Add delete function also
    # PUT

class PostRetrieveDeleteAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self,request,id=None):
        post=get_object_or_404(Post,id=id)
        serializer=PostSerializer(post,data=request.data,context={'request':request})
        if serializer.is_valid():
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        print('it called')
        try:
            post = Post.objects.get(id=id)
            post.delete()
            return Response({'message': "Post successfully deleted"}, status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

class LikeListCreateView(APIView):
    pass
# GET and POST 

class CommentListCreateView(APIView):
    pass

# GET & POST


