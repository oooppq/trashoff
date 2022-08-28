from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('<int:place_id>/', get_trashcans, name='get_trashcans'),
    path('<int:place_id>/<int:trashcan_id>/increase/', increase_trash, name='increase_trash'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)