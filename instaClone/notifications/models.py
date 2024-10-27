from django.db import models
from accounts.models import InstaUser
from django.utils import timezone

class Notifications(models.Model):
    receipient=models.ForeignKey(InstaUser,related_name='notifications',on_delete=models.CASCADE)
    sender=models.ForeignKey(InstaUser,related_name='sent_notification',on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(default=timezone.now)
    is_read=models.BooleanField(default=False)

    def __str__(self):
        return f"Notification from {self.sender}"
    


