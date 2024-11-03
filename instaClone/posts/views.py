from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from . serializer import *
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.parsers import MultiPartParser,FormParser
from django.db.models import Count

class PostListCreateApi(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self,request,*args,**kwargs):
        # List all post and there like count and comment_count
        data=Post.objects.all().annotate(like_count=Count('likes')).annotate(comment_count=Count('comment')).order_by('-created_at')
        serializer=PostSerializer(data,many=True,context={'request': request})
        return Response(serializer.data)
    
    def post(self,request):
        data=request.data
        serializer=PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

class PostRetrieveDeleteAPI(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        serializer = PostSerializer(post, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Cause of error is not add slash - remember
    def delete(self, request, id=None):
        post = get_object_or_404(Post, id=id)
        post.delete()
        return Response({'message': "Post successfully deleted"}, status=status.HTTP_200_OK)

class LikeCountCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        post_id = request.data.get("post")  
        post = get_object_or_404(Post, id=post_id)

        # Check if the user has already liked this post
        if Like.objects.filter(user=request.user, post=post).exists():
            return Response({"message": "You have already liked this post."}, status=status.HTTP_400_BAD_REQUEST)

        # Create a like instance if it doesn't exist
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CommentListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        comment=Comment.objects.all().order_by('-timestamp')
        serializer=CommentSerializer(comment,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(Self,request):
        serializer=CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



