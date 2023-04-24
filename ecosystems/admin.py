from django.contrib import admin
from .models import Ecosystem

# Register your models here.
class EcosystemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'website', 'date_added')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_per_page = 25

admin.site.register(Ecosystem, EcosystemAdmin)