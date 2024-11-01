from django.db import models
from accounts.models import *

class Post(models.Model):
    author=models.ForeignKey(InstaUser,on_delete=models.CASCADE,related_name='posts')
    images=models.ImageField(upload_to='posts/', blank=True, null=True)
    caption=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.author.username} on {self.created_at}'
    
class Like(models.Model):
    user=models.ForeignKey(InstaUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    is_like=models.BooleanField(default=False)

    class Meta:
        unique_together=('user','post')

    def __str__(self):
        return f"{self.user} likes {self.post}"
    
class Comment(models.Model):
    user=models.ForeignKey(InstaUser,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    timestamp=models.DateTimeField(auto_now_add=True)
    content=models.TextField()

    def __str__(self):
        return f"{self.user} comment on {self.post} . "

