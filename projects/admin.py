from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner')
    search_fields = ('name',)
    list_filter = ('owner',)

admin.site.register(Project, ProjectAdmin)
# Register your models here.
