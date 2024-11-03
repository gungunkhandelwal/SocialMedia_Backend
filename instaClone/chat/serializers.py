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

    def create(self,validated_data):
        participants=validated_data.get('participants',[])
        if self.context['request'].user not in participants:
            participants.append(self.context['request'].user)
        validated_data['participants']=participants
        return super().create(validated_data)
#    NotImplementedError: `create()` must be implemented.   