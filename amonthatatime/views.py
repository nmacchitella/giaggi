from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, PostImage, Image
import math

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from .models import Subscriber
from .forms import SubscriberForm
from .pythonsupport.views import random_digits


# Create your views here.

#archive//all month
def archive(request):
    latest_posts = Post.objects.filter(status=1).order_by('-year','-month_number')[:12]
    logo = Image.objects.get(title='calvinandhobbes')
    context = {'latest_posts': latest_posts, 'logo':logo,}
    return render(request, 'amonthatatime/archive.html', context)

#Post
def post(request, year, month):
    post = Post.objects.get(month=month,year=year,status=1)
    photos = PostImage.objects.filter(post=post)
    logo = Image.objects.get(title='calvinandhobbes')

    context = {
        'post': post,
        'photos':photos,
        'logo':logo,
        }
    return render(request, 'amonthatatime/post.html', context)

#Subscribe
@csrf_exempt
def subscribe(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/amonthatatime'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'amonthatatime/index.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'amonthatatime/index.html', {'form': SubscriberForm()})

#confirm subscription
def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'amonthatatime/index.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'amonthatatime/index.html', {'email': sub.email, 'action': 'denied'})

#delete subscription
def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'amonthatatime/index.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'amonthatatime/index.html', {'email': sub.email, 'action': 'denied'})
