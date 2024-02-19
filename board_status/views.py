from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BoardStatus
from .serializers import StatusSerializer
from rest_framework import status


class BoardStatusViewSet(APIView):
    queryset = BoardStatus.objects.all()
    serializer_class = StatusSerializer
    
    def get(self, request, format=None):
        stat = BoardStatus.objects.all()
        serializer = StatusSerializer(stat, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def get_queryset(self, pk):
        try:
            stat = BoardStatus.objects.get(id=pk)
            return stat
        except BoardStatus.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def patch(self, request, pk, format=None):
        stat_object = self.get_queryset(pk)

        serializer = StatusSerializer(stat_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        stat = self.get_queryset(pk)
        stat.delete()
        return Response(status.HTTP_204_NO_CONTENT)
