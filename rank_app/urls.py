from django.urls import path
from .views import *
from django.conf import settings

urlpatterns = [
    path('univ_rank', univ_rank, name='univ_rank'),
]