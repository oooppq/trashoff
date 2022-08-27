from codecs import charmap_build
from email.policy import default
from sqlite3 import Timestamp
import string
from django.db import models
from accounts.models import User


class Place(models.Model):
    place_name = models.CharField(max_length=50)  # 장소 이름

    def __str__(self):
        return str(self.place_name)


class Trashcan(models.Model):
    place_id = models.ForeignKey(
        Place, on_delete=models.CASCADE)  # 쓰레기통이 위치한 장소
    trashcan_number = models.IntegerField()  # 쓰레기통 번호


class University(models.Model):
    univ_name = models.CharField(max_length=20, null=True)
    student_num = models.IntegerField(default=0, null=True)
    throw_num = models.IntegerField(default=0, null=True)


class Throwing(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)  # User ID
    trashcan_id = models.ForeignKey(Place, on_delete=models.CASCADE)  # 쓰레기통 ID
    time = models.DateTimeField(auto_now_add=True)  # 쓰레기를 버린 시간


class Quest(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE)  # 장소 id
    title = models.CharField(max_length=100)  # 제목
    content = models.CharField(max_length=200)  # 내용
    quest_level = models.IntegerField(default=0)  # 참여가능한 최소 레벨
    reward = models.CharField(max_length=200)  # 퀘스트 보상
