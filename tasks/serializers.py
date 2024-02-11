from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task

class EditorSerializer(serializers.ModelSerializer ):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        
class TaskSerializer(serializers.ModelSerializer ):
    editor = EditorSerializer
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'editor', 'editor_data']