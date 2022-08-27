from code import interact
import string
from django.db import models
from main_app.models import Place
from accounts.models import User
# Create your models here.


class Quest(models.Model):
    place_id = models.ForeignKey(
        Place, on_delete=models.CASCADE)  # 퀘스트가 이뤄지는 장소
    title = models.CharField(max_length=100)  # 퀘스트 제목
    content = models.CharField(max_length=200)  # 퀘스트 설명
    level = models.IntegerField(default=100)  # 참여가능한 최소 레벨
    reward = models.CharField(default="", max_length=100)  # 퀘스트 보상

# 유저가 성공한 퀘스트 목록
class QuestUser(models.Model):
    quest_id = models.ForeignKey(Quest, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
