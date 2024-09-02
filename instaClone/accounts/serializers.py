from rest_framework import serializers
from .models import *

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstaUser
        fields=['email','username','password','first_name','last_name']

    def validate(self, data):
        if data['username']:
            if InstaUser.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('Username is taken')
            
        if data['email']:
            if InstaUser.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('Email is taken')
        return data
    

    def create(self,validate_data):
        user=InstaUser.objects.create(
            username=validate_data['username'],
            email=validate_data['email'],
            first_name=validate_data['first_name'],
            last_name=validate_data['last_name']       
        )
        user.set_password(validate_data['password'])
        user.save()
        return validate_data

class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=InstaUser
        fields=['profile_pic','bio','gender','website','privacy']
        read_only_fields=['username','first_name','last_name']
