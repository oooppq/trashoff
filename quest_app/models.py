from django.db import models
from accounts.models import User
from rank_app.models import Place

# Create your models here.
class Quest(models.Model):
    user = models.ManyToManyField(User, related_name='users')
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE) # 퀘스트가 이뤄지는 장소
    title = models.CharField(max_length=30) # 퀘스트 제목
    content = models.CharField(max_length=200) # 퀘스트 설명
    level = models.IntegerField(default=0)
    reward = models.CharField(max_length=30)