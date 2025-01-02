from django.db import models
from AppOne.models import Books

class Author(models.Model):
    name = models.CharField(max_length=255)
    bio = models.TextField()
    date_of_birth = models.DateField(null=True, blank=True)
    books_published = models.ManyToManyField(Books, related_name='authors')

    def __str__(self):
        return f'{self.id}. {self.name}'