from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    color = models.CharField(max_length=50, null=True)
    
    def full_name(self):
        name = self.first_name + ' ' + self.last_name
        return name
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name