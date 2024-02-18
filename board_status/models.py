from django.db import models
from virtualenv.app_data import read_only

class BoardStatus(models.Model):
    name = models.CharField(max_length=100)
    status_data = read_only
    
    
    def __str__(self):
        return self.name