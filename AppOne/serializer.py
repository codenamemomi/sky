from rest_framework import serializers
from .models import Books

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
        read_only_fields = ['id']  # Add read-only fields for auto-generated fields
        extra_kwargs = {
            'title': {'required': True},  # Add required field validation
            'author': {'required': True}
        }