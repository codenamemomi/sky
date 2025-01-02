from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_date = models.DateField(null=True, blank=True)
    about_book = models.TextField()

    def __str__(self):
        return f'{self.id}. {self.title}'