from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    publication_date = models.DateField(null=True)
    about_book = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.id}. {self.title}'