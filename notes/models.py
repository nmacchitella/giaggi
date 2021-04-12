from django.db import models
from django.template.defaultfilters import truncatechars

# Create your models here.
class Aphorism(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    aphorism = models.TextField(blank=True, default=None, null=True)
    author = models.CharField(max_length=200, default = None, blank=True)
    notes = models.TextField(blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    updated_at = models.DateTimeField(auto_now=True,  null=True)

    def __str__(self):
        return self.aphorism


class Idea(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, default = None, null=True)
    idea = models.TextField(blank=True, default=None, null=True)
    notes = models.TextField(blank=True, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True,  null=True)
    updated_at = models.DateTimeField(auto_now=True,  null=True)

    @property
    def short_description(self):
        return truncatechars(self.title, 100)

    def __str__(self):
        return self.title
