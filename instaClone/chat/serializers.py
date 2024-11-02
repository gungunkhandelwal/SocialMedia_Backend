from . models import *
from rest_framework import serializers

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields=['id','sender','content','timestamp']

class ConverstaionSerializer(serializers.Serializer):
    messages=MessageSerializer(many=True,read_only=True)

    class Meta:
        model=Conversation
        field=['id','participants','messages','created_at']

#    NotImplementedError: `create()` must be implemented.   