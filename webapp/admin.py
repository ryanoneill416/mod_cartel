from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Build, Comment


@admin.register(Build)
class BuildAdmin(SummernoteModelAdmin):
    """
    Registers Buid model in admin panel
    """
    summernote_fields = ('overview', 'specifications', 'plans',
                         'featured_excerpt')
    prepopulated_fields = {'slug': ('member', 'year', 'make', 'model')}
    list_display = ('member', 'year', 'make', 'model', 'publish_date',
                    'is_featured')
    list_filter = ('publish_date', 'is_featured', 'updated_date', 'year')
    search_fields = ['make', 'model', 'year']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Registers Comment model in admin panel
    """
    list_display = ('name', 'body', 'comment_date', 'build')
    list_filter = ('comment_date',)
    search_fields = ['name', 'body']
