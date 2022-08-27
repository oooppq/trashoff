
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

urlpatterns = [
    path('', views.init, name='init'),
    path('login-index/', views.loginIndex, name='login-index'),
    path('login/', views.login, name='login'), 
    path('congrats/', views.congrats,  name='congrats'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('mypage/', views.myPage, name='mypage'),
    path('profile-modify', views.profileModify, name='profile-modify'),
    path('join', views.join, name='join'),
    path('join2', views.join2, name='join2'),
    path('join3', views.join3, name='join3'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
