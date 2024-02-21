from django.contrib.auth.models import User
from rest_framework import serializers
from board_status.models import BoardStatus
from board_status.serializers import StatusSerializer
from .models import Choices, Task

class EditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']
        
        
class AssignedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class ChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        if obj == '' and self.allow_blank:
            return obj
        return self._choices[obj]

    def to_internal_value(self, data):
        if data == '' and self.allow_blank:
            return ''

        for key, val in self._choices.items():
            if val == data:
                return key
        self.fail('invalid_choice', input=data)
        
class TaskSerializer(serializers.ModelSerializer ):
    editor = EditorSerializer
    assigned_to = AssignedToSerializer
    category = ChoiceField(choices=Choices.CATEGORY_LIST)
    priority = ChoiceField(choices=Choices.PRIORITY_LIST)
    status= StatusSerializer
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'editor', 'editor_data', 'category', 'priority', 'status', 'status_data', 'assigned_to', 'color']