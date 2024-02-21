from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import ContactSerializer
from .models import Contact
from rest_framework import status
from rest_framework.response import Response


class ContactViewSet(APIView):
    """
    Contact Queryset Class
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, format=None):
        """
        Get Request for Get all Contact Objects from Contacts DB 
        """
        contacts = Contact.objects.all().order_by('first_name')
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        """
        Post Request for Create Contact Object in Contacts DB 
        """
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
class ContactDetailsViewSet(APIView):
    """
    Contact Details Class
    """
    def get(self, request, pk):
        """
        Get Request for Get Contact Object by pk from Contacts DB 
        """
        try:
            contacts = Contact.objects.filter(id=pk)
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        except Contact.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
    
    
    def get_queryset(self, pk):
        """
        Help Queryset for delete and update contact objects
        """
        try:
            contact = Contact.objects.get(id=pk)
            return contact
        except Contact.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND
        
    
    def delete(self, request, pk, format=None):
        """
        Delete Request for Delete Contact Object by pk in Contacts DB 
        """
        contact = self.get_queryset(pk)
        contact.delete()
        return Response(status.HTTP_204_NO_CONTENT)
    
    
    def patch(self, request, pk, format=None):
        """
        Patch Request for Update Contact Object by pk in Contacts DB 
        """
        contact_object = self.get_queryset(pk)

        serializer = ContactSerializer(contact_object, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status.HTTP_400_BAD_REQUEST)