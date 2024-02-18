from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BoardStatus

from .serializers import StatusSerializer


class BoardStatusViewSet(APIView):
    queryset = BoardStatus.objects.all()
    serializer_class = StatusSerializer
    
    def get(self, request, format=None):
        status = BoardStatus.objects.all()
        serializer = StatusSerializer(status, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
