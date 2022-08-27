from django.shortcuts import render, get_object_or_404
from .models import Quest, QuestUser

# Create your views here.
def quest(request):
    quests = Quest.objects.all()
    user = request.user
    # quest_home.html에서 if문에서 레벨 비교, 현재 양과 목표량 비교 프런트에서..?
    return render(request, 'quest.html', {'quests': quests})

def quest_detail(request, quest_id):
    quest_detail = get_object_or_404(Quest, pk=quest_id)
    return render(request, 'quest_detail.html', {'quest_detail': quest_detail})