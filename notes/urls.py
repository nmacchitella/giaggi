from django.urls import path
from . import views



app_name = 'notes'

urlpatterns = [
    # ex: /aphorism/
    path('', views.notes, name='notes'),
    # ex: /notes/aphorism
    path('aphorism', views.aphorism, name='aphorism'),
    # ex: /notes/images
    path('ideas', views.ideas, name='ideas'),
]
