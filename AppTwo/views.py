from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializer import AuthorSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404


# Create your views here.

class Authorlist(APIView):
    def get(self, request):
        items = Author.objects.all()
        serializer = AuthorSerializer(items, many= True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class AuthorDetail(APIView):
    def get(self, request, pk):
        item = get_object_or_404(Author, pk=pk)
        serializer = AuthorSerializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = AuthorSerializer(item, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            item = Author.objects.get(pk=pk)
        except Author.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
