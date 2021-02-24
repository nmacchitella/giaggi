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
from django.db import IntegrityError
import django.template.loader as t_loader




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
    try:
        if request.method == 'POST':
            sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
            sub.save()
            logo = Image.objects.get(title='calvinandhobbes')
            confirmation=t_loader.get_template('amonthatatime/confirmation.html').render({'url':request.build_absolute_uri('/amonthatatime'),'email':sub.email,'logo':logo,'conf_num':sub.conf_num})

            message = Mail(
                from_email=(settings.FROM_EMAIL,'A Month at a Time'),
                to_emails=sub.email,
                subject='A Month at a Time - Email Confirmation',
                html_content=confirmation)

            sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
            response = sg.send(message)
            return render(request, 'amonthatatime/subscribe.html', {'email': sub.email,'action':'just_subscribed'})
        else:
            return render(request, 'amonthatatime/subscribe.html', {'form': SubscriberForm(), 'action':'unknown'})
    except IntegrityError as e:
        return render(request, 'amonthatatime/subscribe.html', {'email': sub.email,'action':'existing'})
    except KeyError as e:
        return render(request, 'amonthatatime/subscribe.html', {'action': 'denied'})




#confirm subscription
def confirm(request):
    try:
        sub = Subscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            sub.confirmed = True
            sub.save()
            return render(request, 'amonthatatime/subscribe.html', {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, 'amonthatatime/subscribe.html', {'email': sub.email, 'action': 'denied'})
    except KeyError as e:
        return render(request, 'amonthatatime/subscribe.html', {'action': 'denied'})

#delete subscription
def delete(request):
    try:
        sub = Subscriber.objects.get(email=request.GET['email'])
        if sub.conf_num == request.GET['conf_num']:
            sub.delete()
            return render(request, 'amonthatatime/subscribe.html', {'email': sub.email, 'action': 'unsubscribed'})
        else:
            return render(request, 'amonthatatime/subscribe.html', {'email': sub.email, 'action': 'denied'})
    except KeyError as e:
        return render(request, 'amonthatatime/subscribe.html', {'action': 'denied'})
