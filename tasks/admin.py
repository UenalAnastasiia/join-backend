from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('title','description', 'due_date', 'editor')
    list_display = ('id', 'title', 'due_date', 'editor')
    search_fields = ('text',)

admin.site.register(Task, TaskAdmin)