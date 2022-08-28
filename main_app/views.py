from unicodedata import name
from django.shortcuts import render
from .models import Place, Trashcan, Throwing
from accounts.models import User
from rank_app.models import University
# Create your views here.


def home(request):
    return render(request, 'index.html')


def get_trashcans(request, place_id=1):
    trashcans = Trashcan.objects.filter(place_id=place_id)

    if trashcans.exists() is False:
        print("쓰레기통 없음")

    map_page = "map" + str(place_id) + ".html"
    return render(request, map_page, {'trashcans': trashcans})


def increase_trash(request, place_id=1, trashcan_id=1):
    try:
        user = request.user

        user.cleanTrashNumber += 1
        user.save()

        print("user 횟수 :", user.cleanTrashNumber)
    except Exception as error:
        print(error, ": 사용자를 찾을 수 없습니다.")

    try:
        university = University.objects.get(name=user.university)

        university.throw_num += 1
        university.save()
        print("university 횟수 :", university.throw_num)
    except Exception as error:
        print(error, ": 사용자의 소속 대학이 없습니다.")

    trashcan = Trashcan.objects.get(place_id=place_id, id=trashcan_id)
    Throwing.objects.create(user_id=request.user, trashcan_id=trashcan)

    map_page = "map" + str(place_id) + ".html"
    return render(request, map_page)
