from FriendRequest.models import FriendRequest
from . models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=FriendRequest)
def create_friend_request_notification(sender,instance,created,**kwargs):
    if created:
        Notifications.objects.create(
            receipient=instance.receiver,
            sender=instance.sender,
            message=f"{instance.sender.username} sent you a follow request."
        )