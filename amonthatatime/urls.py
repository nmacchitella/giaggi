from django.urls import path
from . import views


app_name = 'amonthatatime'

urlpatterns = [
    # ex: /amonthatatime/
    path('', views.archive, name='archive'),
    # ex: /2021/january/
    path('<int:year>/<str:month>/', views.post, name='post'),
    #subscribers
    path('subcribe/', views.subcribe, name='subcribe'),
    path('confirm/', views.confirm, name='confirm'),
    path('delete/', views.delete, name='delete'),

]
