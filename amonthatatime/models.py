from django.db import models
from django.contrib.auth.models import User
import os
import base64
from .pythonsupport.models import newletter_gram_path, folder_upload
from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import django.template.loader as t_loader
from cloudinary.models import CloudinaryField
import cloudinary
import datetime


STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

COLUMNS = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    )

MONTH = (
    ("january","January"),
    ("february","February"),
    ("march","March"),
    ("april","April"),
    ("may","May"),
    ("june","June"),
    ("july","July"),
    ("august","August"),
    ("september","September"),
    ("october","October"),
    ("november","November"),
    ("december","December"),
    )

FOLDERS = (
    ("general","general"),
)

# Create your models here.
class Post(models.Model):
    year = models.IntegerField(default='2021')
    month = models.CharField(max_length=20, choices=MONTH)
    month_number=models.IntegerField(default='1')
    title = models.CharField(max_length=200)
    whatsapp = models.TextField()
    medley = models.TextField()
    photo_columns = models.IntegerField(choices=COLUMNS, default=4)

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    #slug = models.SlugField(max_length=200, unique=True)
    #author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')

    class Meta:
        ordering = ['-created_on']
        unique_together = ('year', 'month',)

    def __str__(self):
        return self.title

    def send(self, request):

        photos = PostImage.objects.filter(post=self)
        contents = t_loader.get_template('amonthatatime/newsletter.html').render({'post':self,'photos':photos,})
        subscribers = Subscriber.objects.filter(confirmed=True)
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)

        for sub in subscribers:
            message = Mail(
                    from_email=settings.FROM_EMAIL,
                    to_emails=sub.email,
                    subject='A month at a Time - {month} {year}: {title}'.format(month=self.month ,year=self.year,title=self.title),
                    html_content=contents + (
                        '<br><a href="{}/delete/?email={}&conf_num={}">Unsubscribe</a>.').format(
                            request.build_absolute_uri('/delete/'),
                            sub.email,
                            sub.conf_num))
            sg.send(message)

    def save(self, *args, **kwargs):
        self.month_number=datetime.datetime.strptime(self.month, "%B").month
        super(Post, self).save(*args, **kwargs)




class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    grams = models.FileField(upload_to = newletter_gram_path)
    urls=models.TextField(default='na')
    caption = models.TextField(default=0)

    def save(self, *args, **kwargs):
        #if os.environ.get('DJANGO_DEVELOPMENT')=="True":
        #    self.urls=self.grams.url
        #    super(PostImage, self).save(*args, **kwargs)
        #else:
        cloudinary.config( cloud_name = "giaggi", api_key = "826931829168994", api_secret = os.environ.get('CLOUDINARY_API_SECRET') )
        upload=cloudinary.uploader.upload(self.grams.open(),
                                            folder=newletter_gram_path(self,self.grams.name),
                                            use_filename=True,
                                            unique_filename=False,
                                            overwrite=True)
        self.urls=upload['url']
        super(PostImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.post.title

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    conf_num = models.CharField(max_length=15)
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.email + " (" + ("not " if not self.confirmed else "") + "confirmed)"


class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='htmls')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")





class Image(models.Model):
    folder=models.CharField(max_length=20, choices=FOLDERS)
    title=models.CharField(max_length=40, default='na')
    photo = models.FileField(upload_to = folder_upload)
    urls=models.TextField(default='na')


    def save(self, *args, **kwargs):
    #    if os.environ.get('DJANGO_DEVELOPMENT')=="True":
    #        self.urls=self.photo.url
    #        super(Image, self).save(*args, **kwargs)
    #    else:
        cloudinary.config( cloud_name = "giaggi", api_key = "826931829168994", api_secret = os.environ.get('CLOUDINARY_API_SECRET') )
        upload=cloudinary.uploader.upload(self.photo.open(),
                                            folder='amonthatatime/images/{folder}'.format(folder=self.folder),
                                            use_filename=True,
                                            unique_filename=False,
                                            overwrite=True)
        self.urls=upload['url']
        super(Image, self).save(*args, **kwargs)
