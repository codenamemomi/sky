from django.urls import path
from .views import Booklist, Bookdetail

urlpatterns = [
    path('books/', Booklist.as_view(), name='books-list'),
    path('books/<int:pk>/', Bookdetail.as_view(), name='book-detail'),
]