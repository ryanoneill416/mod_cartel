from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Build


@admin.register(Build)
class BuildAdmin(SummernoteModelAdmin):
    summernote_fields = ('overview', 'specifications', 'plans', 'featured_excerpt')
    prepopulated_fields = {'slug': ('member', 'year', 'make', 'model')}
    list_display = ('member', 'year', 'make', 'model', 'publish_date', 'is_featured')
    list_filter = ('publish_date', 'is_featured', 'updated_date', 'year')
    search_fields = ['make', 'model', 'year']
