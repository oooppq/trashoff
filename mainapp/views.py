from turtle import title
from django.shortcuts import render
from .models import *

def get_quests(request, place=None):
    quests = Quest.objects.filter(place_id=place).values(title, quest_level)
    
    return render(request, 'main.html', {'quests' : quests} )