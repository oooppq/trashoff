from unicodedata import name
from django.shortcuts import render
from .models import Place, Trashcan, Throwing
from accounts.models import User
from rank_app.models import University
# Create your views here.


def home(request):
    return render(request, 'index.html')


def get_trashcans(request, map_number):
    trashcans = Trashcan.objects.filter(map_number=map_number)
    map_page = "map" + str(map_number) + ".html"
    return render(request, map_page, {'trashcans': trashcans})

def increase_trash(request):
    user = request.user
    
    user.cleanTrashNumber += 1
    
    university = University.objects.get(name=user.university)
    university.throw_num += 1