from django.urls import path
from .views import Booklist

urlpatterns =[
    path('books/', Booklist.as_view(), name='books-list'),
    path('books/<int:pk>/',Booklist.as_view(),name='books_detail'),
]
