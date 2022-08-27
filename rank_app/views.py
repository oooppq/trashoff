from django.shortcuts import render
from .models import University
from accounts.models import User
# Create your views here.


def ranking(request):
    univs = University.objects.filter().order_by('-throw_num')
    return render(request, 'ranking.html', {'univs': univs})
