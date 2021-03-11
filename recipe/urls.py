from django.urls import path
from . import views



app_name = 'recipe'

urlpatterns = [
    # ex: /recipe/
    path('', views.cookbook, name='cookbook'),
    # ex: /recipe/1
    path('<int:id>', views.recipe, name='recipe'),
]
