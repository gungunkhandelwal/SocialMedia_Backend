from . models import *
from rest_framework import serializers

class FriendRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendRequest
        fields = '__all__'

    def create(self, validated_data):
        sender = self.context['request'].user  
        receiver=validated_data.get('receiver')

        if sender == receiver:
            raise serializers.ValidationError('You cannot send a friend request to yourself')
        
        if FriendRequest.objects.filter(sender=sender,receiver=receiver).exists():
            raise serializers.ValidationError("Friend request already sent")
        validated_data.pop('sender', None)
        return FriendRequest.objects.create(sender=sender,**validated_data)
