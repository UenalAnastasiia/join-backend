from os import error
from xmlrpc.client import ResponseError
from django.views.defaults import ERROR_400_TEMPLATE_NAME
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response


class TaskViewSet(APIView):
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    
    def get(self, request, format=None):
        tasks = Task.objects.all().order_by('due_date')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TaskDetailsViewSet(APIView):
    def get(self, request, pk):
        try:
            tasks = Task.objects.filter(id=pk)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        try:
            task = Task.objects.get(id=pk)
            return task
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        task = self.get_queryset(pk)
        task.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk, format=None):
        task_object = self.get_queryset(pk)

        serializer = TaskSerializer(task_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)