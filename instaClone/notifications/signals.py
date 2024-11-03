from FriendRequest.models import FriendRequest
from . models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from posts.models import Like , Comment
@receiver(post_save,sender=FriendRequest)
def create_friend_request_notification(sender,instance,created,**kwargs):
    if created:
        Notifications.objects.create(
            receipient=instance.receiver,
            sender=instance.sender,
            message=f"{instance.sender.username} sent you a follow request."
        )
    
@receiver(post_save,sender=Like)
def like_post_notification(sender,instance,created,**kwargs):
    if created:
        Notifications.objects.create(
            receipient=instance.post.author,
            sender=instance.user,
            message=f"{instance.user.username} likes your post"
        )

@receiver(post_save,sender=Comment)
def comment_post_notification(sender,instance,created,**kwargs):
    if created:
        Notifications.objects.create(
            receipient=instance.post.author,
            sender=instance.user,
            message=f"{instance.user.username} comments on your post {instance.content}"
        )
