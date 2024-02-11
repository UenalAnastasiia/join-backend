from rest_framework.views import APIView
from .serializers import TaskSerializer
from .models import Task
from rest_framework import status
from rest_framework.response import Response


class TaskViewSet(APIView):
    queryset = Task.objects.all().order_by('due_date')
    serializer_class = TaskSerializer
    
    def get(self, request, format=None):
        todos = Task.objects.filter()
        serializer = TaskSerializer(todos, many=True)
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
            todos = Task.objects.filter(id=pk)
            serializer = TaskSerializer(todos, many=True)
            return Response(serializer.data)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        try:
            return Task.objects.get(editor=self.request.user, id=pk)
        except Task.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        todo = self.get_queryset(pk)
        todo.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk, format=None):
        todoItem_object = self.get_queryset(pk)
        print('pk ', todoItem_object)

        serializer = TaskSerializer(todoItem_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)