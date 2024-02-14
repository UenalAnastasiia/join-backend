from django.contrib import admin

from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    fields = ('first_name','last_name', 'email', 'phone')
    list_display = ('first_name','last_name', 'email', 'phone')
    search_fields = ('text',)

admin.site.register(Contact, ContactAdmin)
