from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Books
from .serializer import BooksSerializer
from rest_framework import status

# Create 
# your views here.

class Booklist(APIView):
    def get(self, request):
        items = Books.objects.all().values()
        serializer = BooksSerializer(items, many= True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def put(self,request,pk):
        try:
            item = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = BooksSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            item = Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
    
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
