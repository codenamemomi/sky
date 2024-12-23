# Generated by Django 5.1.4 on 2024-12-22 19:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AppOne', '0002_alter_books_about_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('bio', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField(null=True)),
                ('books_published', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='AppOne.books')),
            ],
        ),
    ]
