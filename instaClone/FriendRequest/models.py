from django.db import models
from accounts.models import *

class FriendRequest(models.Model):
    sender=models.ForeignKey(InstaUser,related_name='sent_friend_request',on_delete=models.CASCADE)
    receiver=models.ForeignKey(InstaUser,related_name='receive_friend_request',on_delete=models.CASCADE)
    is_accepted=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('sender','receiver')

    def __str__(self):
        return f"{self.sender} -> {self.receiver}"
