from django.db import models
from AppOne.models import Books
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=25)
    bio = models.CharField(max_length=200)
    date_of_birth = models.DateField(null=True)
    books_published = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='authors')
