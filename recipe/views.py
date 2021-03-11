from django.shortcuts import render
from django.http import HttpResponse
from .models import Recipe, Reference


# Create your views here.
def cookbook(request):
    all_recipes = Recipe.objects.all()
    context = {'all_recipes': all_recipes}
    return render(request, 'recipe/cookbook.html', context)

def recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    try:
        reference = Reference.objects.filter(recipe=recipe)
    except:
        reference = None
    context = {'recipe': recipe, 'reference': reference}
    return render(request, 'recipe/recipe.html', context)
