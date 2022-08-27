from django.db import models
from accounts.models import User
from rank_app.models import Place

# Create your models here.
class Quest(models.Model):
    user = models.ManyToManyField(User, through='QuestUser')
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE) # 퀘스트가 이뤄지는 장소
    title = models.CharField(max_length=30) # 퀘스트 제목
    content = models.CharField(max_length=200) # 퀘스트 설명
    level = models.IntegerField(default=0) # 퀘스트 참가 최소 레벨
    goal = models.IntegerField(default=100) # 퀘스트 목표
    reward = models.CharField(max_length=30) # 퀘스트 보상

    def __str__(self):
        return self.title

class QuestUser(models.Model):
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
