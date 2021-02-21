from django.contrib import admin
from .models import Post, PostImage, Subscriber, Newsletter, Image
from django_summernote.admin import SummernoteModelAdmin


class PostImageAdmin(admin.StackedInline):
    model = PostImage
    extra = 0
    exclude = ('urls',)


def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Newsletters to all subscribers"

class PostAdmin(SummernoteModelAdmin):
    list_display = ('year', 'month', 'title', 'created_on', 'updated_on', 'status')
    list_filter = ("status",)
    search_fields = ['title', 'month', 'year', 'whatsapp' ]
    inlines = [PostImageAdmin]
    summernote_fields = '__all__'
    class Meta:
       model = Post

    actions = [send_newsletter]
    exclude = ('month_number',)


class PostImageAdmin(admin.ModelAdmin):
    pass


class ImageAdmin(admin.ModelAdmin):
    exclude = ('urls',)
    list_display = ('folder', 'title', 'urls')






# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Subscriber)
admin.site.register(Image,ImageAdmin)
