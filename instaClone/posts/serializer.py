from . models import *
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    author_username=serializers.ReadOnlyField(source='author.username')
    class Meta:
        model=Post
        fields=['id','author_username','images','caption','created_at']
        read_only_field=['author,created_at']


     


