from django.urls import path
from .views import Authorlist, AuthorDetail

urlpatterns =[
    path('authors/',Authorlist.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
]