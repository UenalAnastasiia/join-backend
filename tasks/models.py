from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from board_status.models import BoardStatus

from contacts.models import Contact


class Choices(models.Model):
    CATEGORY_LIST = ((1, 'Frontend'), (2, 'Backend'), (3, 'Design'), (4, 'Marketing'), (5, 'Backoffice'), (6, 'Other'))
    PRIORITY_LIST = ((1, 'urgent'), (2, 'medium'), (3, 'low'), (4, 'Archived'))

class Task(models.Model):
    editor = models.ForeignKey(User, related_name='editor', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    due_date  = models.DateField()
    category = models.IntegerField(choices=Choices.CATEGORY_LIST, null=True)
    priority = models.IntegerField(choices=Choices.PRIORITY_LIST, null=True)
    status = models.ForeignKey(BoardStatus, on_delete=models.CASCADE, null=True)
    assigned_to = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True)
    color = models.CharField(max_length=50, null=True)
    
    
    def editor_data(self):
        return {'username': self.editor.username, 'first_name': self.editor.first_name, 'last_name': self.editor.last_name}
    
    
    def status_data(self):
        return {'id': self.status.id, 'name': self.status.name}