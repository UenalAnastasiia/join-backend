from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Contact


class ContactSerializer(serializers.ModelSerializer ):
    
    class Meta:
        model = Contact
        fields = ['id', 'first_name','last_name', 'email', 'phone', 'color', 'full_name']