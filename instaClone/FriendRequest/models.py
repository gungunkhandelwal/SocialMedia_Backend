from django.db import models
from accounts.models import *

class FriendRequest(models.Model):
    sender = models.ForeignKey(InstaUser, related_name='sent_requests', on_delete=models.CASCADE)
    receiver = models.ForeignKey(InstaUser, related_name='received_requests', on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('sender', 'receiver')  #Only once sender can send friend request

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"

class Following(models.Model):
    user=models.ForeignKey(InstaUser,related_name="following",on_delete=models.CASCADE)
    following=models.ForeignKey(InstaUser,related_name="followers",on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','following')

    def __str__(self):
        return f"{self.user.username} follows {self.following.username}"
