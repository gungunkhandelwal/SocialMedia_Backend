from django.db import models
from django.contrib.auth.models import AbstractUser

Gender=(
    (1,'Male'),
    (2,'Female'),
    (3,'Other')
    )

class InstaUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='profile_pics/',blank=True, null=True)
    bio=models.CharField(max_length=200,blank=True)
    website=models.URLField(max_length=250,blank=True)
    gender=models.IntegerField(choices=Gender,blank=True,null=True)
    privacy=models.BooleanField(default=False)

