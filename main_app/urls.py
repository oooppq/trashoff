from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('<int:place_id>/', get_trashcans, name='get_trashcans'),
    path('<int:place_id>/increase/', increase_trash, name='increase_trash'),
]
