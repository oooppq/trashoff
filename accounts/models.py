from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20, null=True)
    photo = models.ImageField(upload_to='profileImg/', blank=True)
    university = models.CharField(max_length=20, null=True)
    cleanTrashNumber = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    date = models.DateTimeField(auto_now_add=True, null=True)
    
    