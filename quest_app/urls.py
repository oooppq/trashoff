from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('quest_detail/<int:quest_id>/', quest_detail, name='quest_detail'),
]