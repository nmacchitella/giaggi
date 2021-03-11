from django.db import models
from taggit.managers import TaggableManager
import uuid



# Create your models here.
class Recipe(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default = None)
    servings = models.IntegerField()
    ingredient = models.TextField(blank=True, default=None, null=True)
    notes = models.TextField(blank=True, default=None, null=True)
    tags = TaggableManager(blank=True)


    def __str__(self):
        return self.title


class Reference(models.Model):
    recipe = models.ForeignKey(Recipe, default=None, on_delete=models.CASCADE)
    url = models.URLField()

    def __str__(self):
        return self.url
