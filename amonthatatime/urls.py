from django.urls import path
from . import views


app_name = 'amonthatatime'

urlpatterns = [
    # ex: /amonthatatime/
    path('', views.archive, name='archive'),
    # ex: /2021/january/
    path('<int:year>/<str:month>/', views.newsletter, name='newsletter'),

]
