from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', ranking, name='rank'),
    path('main/', include('main_app.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)