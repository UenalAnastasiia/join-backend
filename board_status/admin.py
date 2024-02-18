from django.contrib import admin

from .models import BoardStatus

class BoardStatusAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['id', 'name']

admin.site.register(BoardStatus, BoardStatusAdmin)