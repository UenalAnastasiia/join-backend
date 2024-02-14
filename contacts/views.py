from django.shortcuts import render

from rest_framework.views import APIView
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import status
from rest_framework.response import Response


class ContactViewSet(APIView):
    queryset = Contact.objects.all().order_by('first_name')
    serializer_class = ContactSerializer
    
    def get(self, request, format=None):
        contacts = Contact.objects.filter()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ContactDetailsViewSet(APIView):
    def get(self, request, pk):
        try:
            contacts = Contact.objects.filter(id=pk)
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        try:
            contact = Contact.objects.get(id=pk)
            return contact
        except Contact.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        contact = self.get_queryset(pk)
        contact.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk, format=None):
        contact_object = self.get_queryset(pk)

        serializer = ContactSerializer(contact_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)