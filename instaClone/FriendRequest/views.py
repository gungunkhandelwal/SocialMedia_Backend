from django.shortcuts import render
from . models import *
from . serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

# class FriendRequestView(APIView):
#     permission_classes = [IsAuthenticated]

#     def post(self, request):
#         serializer = FriendRequestSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FriendRequestViewSet(viewsets.ModelViewSet):
    serializer_class=FriendRequestSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        return FriendRequest.objects.filter(
            receiver=self.request.user,
            is_accepted=False
        )
    
    def create(self,request,*args,**kwargs):
        serializer=self.get_serializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    @action(detail=False,methods=['get'],url_path='sent_requests')
    def send_requests(self,request):
        # Get request sent by current user
        sent_requests=FriendRequest.objects.filter(
            sender=request.user,
            is_accepted=False
        )
        serializer=self.get_serializer(sent_requests,many=True)
        return Response(serializer.data)
    
    @action(detail=True,methods=['post'])
    def accept(self,request, pk=None):
        friend_request=self.get_object()
        if friend_request.receiver != request.user:
            return Response(
                {"error":"You can only accept request sent to you"},
                status=status.HTTP_403_FORBIDDEN
            )
        friend_request.is_accepted=True
        friend_request.save()

        Following.objects.create(
            user=friend_request.sender,
            following=friend_request.receiver
        )
        Following.objects.create(
            user=friend_request.receiver,
            following=friend_request.sender
        )
        
        return Response({"message": "Friend request accepted"})
        
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        friend_request = self.get_object()
        
        if friend_request.receiver != request.user:
            return Response(
                {"error": "You can only reject requests sent to you"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        friend_request.delete()
        return Response({"message": "Friend request rejected"})
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        friend_request = self.get_object()
        
        if friend_request.sender != request.user:
            return Response(
                {"error": "You can only cancel requests you sent"},
                status=status.HTTP_403_FORBIDDEN
            )
        
        friend_request.delete()
        return Response({"message": "Friend request cancelled"})

class ConnectionViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class=FollowingSerializer
    permission_classes=[IsAuthenticated]

    def get_queryset(self):
        # Default queryset for list view - user's followers
        return Following.objects.filter(following=self.request.user)
    
    @action(detail=False, methods=['get'])
    def following(self, request):
        # Get users that the current user follows
        following=Following.objects.filter(user=request.user)
        serializer=self.get_serializer(following,many=True)
        return Response(serializer.data)
    
    @action(detail=False,methods=['get'])
    def followers(self,request):
        # Get users who follow the current user

        followers=self.get_queryset()
        serializer=self.get_serializer(followers,many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def stats(self, request):
        # Get follower and following counts
        followers_count = self.get_queryset().count()
        following_count = Following.objects.filter(user=request.user).count()
        
        return Response({
            'followers_count': followers_count,
            'following_count': following_count
        })
    




    
    

    


