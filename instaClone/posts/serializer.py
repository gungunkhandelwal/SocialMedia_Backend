from . models import *
from rest_framework import serializers
from django.db.models import Count

class PostSerializer(serializers.ModelSerializer):
    author_username=serializers.ReadOnlyField(source='author.username')
    author_profile_pic=serializers.SerializerMethodField()
    like_count = serializers.IntegerField(read_only=True) #Adding integerField work not serializerMethodField
    comment_count=serializers.IntegerField(read_only=True)

    class Meta:
        model=Post
        fields=['id','author_username','author_profile_pic','images','caption','created_at','like_count','comment_count']
        read_only_field=['author_username','created_at']
    
    def get_author_profile_pic(self, obj):
        request = self.context.get('request')
        if request and obj.author.profile_pic:
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
        



class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for user profile information
    """
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    posts_count = serializers.SerializerMethodField()
    posts = serializers.SerializerMethodField()
    profile_pic = serializers.SerializerMethodField()

    class Meta:
        model = InstaUser
        fields = [
            'id', 
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'bio', 
            'website', 
            'gender', 
            'profile_pic',
            'followers_count', 
            'following_count', 
            'posts_count', 
            'posts'
        ]

    def get_profile_pic(self, obj):
        """
        Get absolute URL for profile picture
        """
        request = self.context.get('request')
        if obj.profile_pic:
            return request.build_absolute_uri(obj.profile_pic.url)
        return None

    def get_followers_count(self, obj):
        """
        Get number of followers
        Note: You'll need to implement a Follow model for this to work
        """
        # Placeholder - replace with actual follower counting logic
        return 0

    def get_following_count(self, obj):
        """
        Get number of users this user is following
        Note: You'll need to implement a Follow model for this to work
        """
        # Placeholder - replace with actual following counting logic
        return 0

    def get_posts_count(self, obj):
        """
        Get total number of posts by the user
        """
        return obj.posts.count()

    def get_posts(self, obj):
        """
        Get detailed information about user's posts
        """
        # Use the PostSerializer you've already defined
        posts = obj.posts.all().annotate(
            like_count=Count('likes', filter=models.Q(likes__is_like=True)),
            comment_count=Count('comment')
        )
        request = self.context.get('request')
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return serializer.data
