from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PostImage
import math


# Create your views here.
def archive(request):
    latest_posts = Post.objects.filter(status=1).order_by('year','month')[:12]
    context = {'latest_posts': latest_posts}
    return render(request, 'amonthatatime/archive.html', context)

def newsletter(request, year, month):
    post = Post.objects.get(month=month,year=year,status=1)
    photos = PostImage.objects.filter(post=post)

    context = {
        'post': post,
        'photos':photos,
        }
    return render(request, 'amonthatatime/newsletter.html', context)

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
