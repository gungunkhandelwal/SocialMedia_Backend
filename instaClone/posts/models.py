from django.db import models
from accounts.models import *

class Post(models.Model):
    author=models.ForeignKey(InstaUser,on_delete=models.CASCADE,related_name='posts')
    images=models.ImageField(upload_to='posts/', blank=True, null=True)
    caption=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.author.username} on {self.created_at}'

