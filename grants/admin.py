from django.contrib import admin
from .models import Grant

# Register your models here.
class GrantAdmin(admin.ModelAdmin):
    list_display=('id','title', 'ecosystem', 'project_category', 'date_added', 'is_published', )
    list_display_links = ('id', 'title', )
    list_filter = ('ecosystem', )
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'project_category', 'ecosystem', )
    list_per_page = 25

admin.site.register(Grant, GrantAdmin)