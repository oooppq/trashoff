from django.contrib import admin
from .models import Quest, QuestUser

# Register your models here.
admin.site.register(Quest)
admin.site.register(QuestUser)