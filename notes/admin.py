from django.contrib import admin
from .models import Aphorism, Idea
from django_summernote.admin import SummernoteModelAdmin



class AphorismAdmin(SummernoteModelAdmin):
    list_display = ('author', 'aphorism', 'updated_at')
    search_fields = ['aphorism', 'author']
    summernote_fields = ['notes']

class IdeaAdmin(SummernoteModelAdmin):
    list_display = ('idea', 'notes', 'updated_at')
    summernote_fields = ['notes']



# Register your models here.
admin.site.register(Aphorism, AphorismAdmin)
admin.site.register(Idea, IdeaAdmin)
