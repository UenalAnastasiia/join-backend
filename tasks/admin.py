from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    fields = ('title','description', 'due_date', 'editor', 'category', 'priority', 'status', 'assigned_to')
    list_display = ('id', 'title', 'priority', 'due_date', 'editor')
    search_fields = ('text',)

admin.site.register(Task, TaskAdmin)