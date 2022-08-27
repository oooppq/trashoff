from django.shortcuts import render
from .models import University
from accounts.models import User
# Create your views here.


def univ_rank(request):
    univs = University.objects.filter().order_by('-throw_num')
    return render(request, 'univ_rank.html', {'univs': univs})
