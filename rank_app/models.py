from codecs import charmap_build
from email.policy import default
from sqlite3 import Timestamp
import string
from django.db import models
from accounts.models import User


class Place(models.Model):
    name = models.CharField(max_length=50)  # 장소 이름

    def __str__(self):
        return str(self.name)


class Trashcan(models.Model):
    place_id = models.ForeignKey(
        Place, on_delete=models.CASCADE)  # 쓰레기통이 위치한 장소
    trashcan_number = models.IntegerField()  # 쓰레기통 번호


class University(models.Model):
    name = models.CharField(max_length=20, null=True) # 학교 이름
    student_num = models.IntegerField(default=0, null=True) # 학교에 속한 학생 인원
    throw_num = models.IntegerField(default=0, null=True) # 쓰레기 버린 횟수

    def __str__(self):
        return self.name


class Throwing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # User ID
    trashcan_id = models.ForeignKey(Place, on_delete=models.CASCADE)  # 쓰레기통 ID
    time = models.DateTimeField(auto_now_add=True)  # 쓰레기를 버린 시간
