
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('mypage/', views.myPage, name='mypage'),
    path('profile-modify', views.profileModify, name='profile-modify'),
    path('congrats/', views.congrats, name='congrats'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
