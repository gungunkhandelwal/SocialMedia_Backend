from . models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author_username=serializers.ReadOnlyField(source='author.username')
    author_profile_pic=serializers.SerializerMethodField()
    like_count = serializers.IntegerField(read_only=True) #Adding integerField work not serializerMethodField
    comment_count=serializers.IntegerField(read_only=True)

    class Meta:
        model=Post
        fields=['id','author_username','author_profile_pic','images','caption','created_at','like_count','comment_count']
        read_only_field=['author_username','created_at']
    
    def get_author_profile_pic(self,obj):
        request=self.context.get('request')
        if obj.author.profile_pic:
            return request.build_absolute_uri(obj.author.profile_pic.url)
        return None
    
    def get_like_count(self,obj):
        return Like.objects.filter(post=obj,is_like=True).count()
    
    def get_comment_count(self,obj):
        return Comment.objects.filter(post=obj).count()


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=['user','post','timestamp']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        



