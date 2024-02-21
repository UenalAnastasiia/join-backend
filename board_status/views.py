from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BoardStatus
from .serializers import StatusSerializer
from rest_framework import status

class BoardStatusViewSet(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """
        Get Request for Get all Board Objects from Board Status DB 
        """
        stat = BoardStatus.objects.all()
        serializer = StatusSerializer(stat, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        """
        Post Request for Create Board Object in Board Status DB 
        """
        serializer = StatusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def get_queryset(self, pk):
        """
        Help Queryset for delete and update board objects
        """
        try:
            stat = BoardStatus.objects.get(id=pk)
            return stat
        except BoardStatus.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def patch(self, request, pk, format=None):
        """
        Patch Request for Update Board Object by pk in Board Status DB 
        """
        stat_object = self.get_queryset(pk)

        serializer = StatusSerializer(stat_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        """
        Delete Request for Delete Board Object by pk in Board Status DB 
        """
        stat = self.get_queryset(pk)
        stat.delete()
        return Response(status.HTTP_204_NO_CONTENT)
