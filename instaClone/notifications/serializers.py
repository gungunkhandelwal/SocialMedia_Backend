from . models import *
from rest_framework import serializers

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notifications
        fields='__all__'
        