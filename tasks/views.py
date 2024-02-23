from os import error
from xmlrpc.client import ResponseError
from django.views.defaults import ERROR_400_TEMPLATE_NAME
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response


class TaskViewSet(APIView):
    """
    Task Queryset Class
    """
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """
        Get Request for Get all Tasks Objects from Tasks DB 
        """
        tasks = Task.objects.all().order_by('due_date')
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        """
        Post Request for Create Task Object in Tasks DB 
        """
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class TaskDetailsViewSet(APIView):
    """
    Task Details Class
    """
    def get(self, request, pk):
        """
        Get Request for Get Task Object by pk from Tasks DB 
        """
        try:
            tasks = Task.objects.filter(id=pk)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        """
        Help Queryset for delete and update task objects
        """
        try:
            task = Task.objects.get(id=pk)
            return task
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        """
        Delete Request for Delete Task Object by pk in Tasks DB 
        """
        task = self.get_queryset(pk)
        task.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk, format=None):
        """
        Patch Request for Update Task Object by pk in Tasks DB 
        """
        task_object = self.get_queryset(pk)

        serializer = TaskSerializer(task_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)