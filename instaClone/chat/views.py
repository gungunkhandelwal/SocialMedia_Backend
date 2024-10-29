from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import *
from . models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

# Add generic classes when backend completed
class ConversationListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request):
        conversation=Conversation.objects.filter(participant=request.user)
        serializer=ConverstaionSerializer(conversation,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        participants=[request.user, *request.data.get('participants',[])]
        serializer=ConverstaionSerializer(data={'paeticipants':participants})

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class MessageListCreateView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,conversation_id):
        message=Message.objects.filter(conversation_id=conversation_id)
        serializer=MessageSerializer(message,many=True)
        print(conversation_id )
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def post(self,request,conversation_id):
        conversation=Conversation.objects.get(id=conversation_id)
        serializer=MessageSerializer(data=request.data)
        print(conversation_id )
        if serializer.is_valid():
            serializer.save(sender=request.user,conversation=conversation)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)