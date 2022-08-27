from django.db import models
from accounts.models import User

# Create your models here.
class Place(models.Model):
    place_name = models.CharField(max_length=20)

class Trashcan(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    

class University(models.Model):
    univ_name = models.CharField(max_length=20, null=True)
    student_num = models.IntegerField(default=0, null=True)
    throw_num = models.IntegerField(default=0, null=True)

class Throwing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    trashcan_id = models.ForeignKey(Trashcan, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)

class Quest(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)