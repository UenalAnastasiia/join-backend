from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Choices(models.Model):
    CATEGORY_LIST = ((1, 'Frontend'), (2, 'Backend'), (3, 'Design'), (4, 'Marketing'), (5, 'Backoffice'), (6, 'Other'))
    PRIORITY_LIST = ((1, 'urgent'), (2, 'medium'), (3, 'low'), (4, 'Archived'))
    STATUS_LIST = ((1, 'To do'), (2, 'In progress'), (3, 'Awaiting Feedback'), (4, 'Done'), (5, 'Archived'))

class Task(models.Model):
    editor = models.ForeignKey(User, related_name='editor', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date  = models.DateField()
    category = models.IntegerField(choices=Choices.CATEGORY_LIST, null=True)
    priority = models.IntegerField(choices=Choices.PRIORITY_LIST, null=True)
    status = models.IntegerField(choices=Choices.STATUS_LIST, null=True)
    assigned_to = models.ForeignKey(User, related_name='assigned_to', on_delete=models.CASCADE, null=True)
    
    
    def editor_data(self):
        return {'username': self.editor.username, 'first_name': self.editor.first_name, 'last_name': self.editor.last_name}