from django.db import models
from django.contrib.auth.models import User
import os
import base64

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




#functios to get the right path to save images of newsletter posts
def newletter_gram_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/post<year>/post<month>/<filename>
    return 'newsletter/{year}/{month}/{file}'.format(year=instance.post.year, month=instance.post.month, file=filename)


# Create your models here.
class Post(models.Model):
    year = models.IntegerField(default='2021')
    month = models.CharField(max_length=20, choices=MONTH)
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


class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    grams = models.FileField(upload_to = newletter_gram_path)
    grams_string=models.TextField(default='na')
    caption = models.TextField(default=0)

    def save(self, *args, **kwargs):

        self.grams_string = base64.b64encode(self.grams.open('rb').read()).decode('utf-8')
        super(PostImage, self).save(*args, **kwargs)

    def __str__(self):
        return self.post.title
