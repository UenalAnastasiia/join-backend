from django.conf import settings
from django.db import models

class Task(models.Model):
    editor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date  = models.DateField()
    # category 
    # priority 
    # status 
    # assigned_to