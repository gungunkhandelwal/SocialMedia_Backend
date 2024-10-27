from django.shortcuts import render
from rest_framework.response import Response
from . serializers import *
from . models import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

class NotificationView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        notification=Notifications.objects.filter(receipient=request.user,is_read=False)
        serializer=NotificationSerializer(notification,many=True)
        print(serializer.data)
        return Response({
            "message": "Follow request is sent",
            "notifications": serializer.data
        })
