from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('<int:place_id>/trashcans', get_trashcans, name='get_trashcans'),
]