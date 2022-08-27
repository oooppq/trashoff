from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', quest, name='quest'),
    path('quest_detail/<int:quest_id>/', quest_detail, name='quest_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)