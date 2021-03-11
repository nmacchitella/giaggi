from django.contrib import admin
from .models import Recipe, Reference
from django_summernote.admin import SummernoteModelAdmin


class ReferenceAdmin(admin.StackedInline):
    model = Reference
    extra = 0

class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'servings', 'tags')
    list_filter = ("tags",)
    search_fields = ['title', 'tags']
    inlines = [ReferenceAdmin]
    summernote_fields = '__all__'
    class Meta:
       model = Recipe


class ReferenceAdmin(admin.ModelAdmin):
    pass



# Register your models here.
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Reference,ReferenceAdmin)
