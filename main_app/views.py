from django.shortcuts import render
from .models import Place, Trashcan, Throwing
from accounts.models import User
# Create your views here.


def home(request):
    return render(request, 'index.html')


def get_trashcans(request, place_id):
    trashcans = Trashcan.objects.filter(place_id=place_id)
    return render(request, 'main.html', {'trashcans': trashcans})
