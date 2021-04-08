from django.shortcuts import render
from .models import Aphorism, Idea


# Create your views here.
def notes(request):
    return render(request, 'notes/notes.html')

def aphorism(request):
    all_aphorism = Aphorism.objects.all().order_by('-updated_at','-created_at')
    context = {'all_aphorism': all_aphorism, }
    return render(request, 'notes/aphorism.html', context)

def ideas(request):
    all_ideas = Idea.objects.all().order_by('-updated_at','-created_at')
    context = {'all_ideas': all_ideas }
    return render(request, 'notes/ideas.html', context)
