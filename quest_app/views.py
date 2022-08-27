from django.shortcuts import render, get_object_or_404
from .models import Quest

# Create your views here.
def quest_home(request):
    quests = Quest.objects.all()
    return render(request, 'quest.html', {'quests': quests})

def quest_detail(request, quest_id):
    quest_detail = get_object_or_404(Quest, pk=quest_id)
    return render(request, 'quest_detail.html', {'quest_detail': quest_detail})