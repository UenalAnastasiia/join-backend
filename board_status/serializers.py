from rest_framework import serializers

from tasks.models import Task
from .models import BoardStatus


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = BoardStatus
        fields = ['id', 'name']
