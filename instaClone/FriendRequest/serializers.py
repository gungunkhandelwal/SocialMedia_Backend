from . models import FriendRequest, Following
from rest_framework import serializers

class FriendRequestSerializer(serializers.ModelSerializer):
    sender_username=serializers.ReadOnlyField(source='sender.username')
    receive_username=serializers.ReadOnlyField(source='receiver.username')

    class Meta:
        model = FriendRequest
        fields = ['id','sender','receiver','is_accepted','created_at','sender_username','receive_username']
        read_only_fields=['sender','is_accepted']

    def create(self, validated_data):
        sender = self.context['request'].user  
        receiver=validated_data.get('receiver')

        if sender == receiver:
            raise serializers.ValidationError('You cannot send a friend request to yourself')
        
        if FriendRequest.objects.filter(sender=sender,receiver=receiver).exists():
            raise serializers.ValidationError("Friend request already sent")
        
        if Following.objects.filter(user=sender,following=receiver).exists():
            raise serializers.ValidationError("Friend request already sent")
        
        existing_request=FriendRequest.objects.filter(sender=receiver,receiver=sender).first()
        if existing_request:
            existing_request.is_accepted=True
            existing_request.save()
            Following.objects.create(user=sender,following=receiver)
            Following.objects.create(user=receiver,following=sender)
            return existing_request
        
        return FriendRequest.objects.create(sender=sender,**validated_data)

class FollowingSerializer(serializers.ModelSerializer):
    username=serializers.ReadOnlyField(source='following.username')

    class Meta:
        model=Following
        fields=['id','user','following','created_at','username']
        read_only_fields=['user']
