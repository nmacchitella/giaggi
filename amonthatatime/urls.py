from django.urls import path
from . import views


app_name = 'amonthatatime'

urlpatterns = [
    # ex: /amonthatatime/
    path('', views.archive, name='archive'),
    # ex: /2021/january/
    path('<int:year>/<str:month>/', views.post, name='post'),
    #subscribers
    path('subscribe/', views.subscribe, name='subscribe'),
    path('confirm/', views.confirm, name='confirm'),
    path('unsubscribe/', views.delete, name='unsubscribe'),

]
