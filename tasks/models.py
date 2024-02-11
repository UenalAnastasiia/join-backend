from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    editor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date  = models.DateField()
    # category 
    # priority 
    # status 
    # assigned_to
    
    
    def editor_data(self):
        return {'username': self.editor.username, 'first_name': self.editor.first_name, 'last_name': self.editor.last_name,}
