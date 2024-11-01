from . models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author_username=serializers.ReadOnlyField(source='author.username')
    author_profile_pic=serializers.SerializerMethodField()
    class Meta:
        model=Post
        fields=['id','author_username','author_profile_pic','images','caption','created_at']
        read_only_field=['author,created_at']
    
    def get_author_profile_pic(self,obj):
        request=self.context.get('request')
        if obj.author.profile_pic:
            return request.build_absolute_uri(obj.author.profile_pic.url)
        return None


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=['user','post','timestamp']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        



