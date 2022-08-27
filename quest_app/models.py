from django.db import models
from rank_app.models import Place

# Create your models here.
class Quest(models.Model):
    place_id = models.ForeignKey(Place, on_delete=models.CASCADE) # 퀘스트가 이뤄지는 장소
    content = models.CharField(max_length=200) # 퀘스트 설명