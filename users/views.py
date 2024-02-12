from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserSerializer

# Create your views here.
class UsersViewSet(APIView):

    def get(self, request, format=None):
        receiverList = User.objects.values('id', 'username', 'first_name', 'last_name', 'email', 'date_joined')
        return Response(receiverList)
    

class UserDetailsViewSet(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.filter(id=pk)
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)
        except User.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND