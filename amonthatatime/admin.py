from django.contrib import admin
from .models import Post, PostImage,Subscriber
from django_summernote.admin import SummernoteModelAdmin

class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 0
    exclude = ('grams_string',)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('year', 'month', 'title', 'created_on', 'updated_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'month', 'year', 'whatsapp' ]
    inlines = [PostImageAdmin]


    summernote_fields = '__all__'

    class Meta:
       model = Post


class PostImageAdmin(admin.ModelAdmin):
    pass





# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)
