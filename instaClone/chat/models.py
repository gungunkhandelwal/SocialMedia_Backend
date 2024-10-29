from django.db import models
from accounts.models import InstaUser

class Conversation(models.Model):
    participant=models.ManyToManyField(InstaUser)
    created_at=models.DateTimeField(auto_now_add=True)

class Message(models.Model):
    conversation=models.ForeignKey(Conversation,related_name='messages',on_delete=models.CASCADE)
    sender=models.ForeignKey(InstaUser,on_delete=models.CASCADE)
    content=models.TextField()
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return  f"{self.sender}:{self.content[:50]}"
