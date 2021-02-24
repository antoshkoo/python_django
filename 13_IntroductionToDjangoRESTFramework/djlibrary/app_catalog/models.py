import datetime

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    date_of_birth = models.DateField(default=datetime.date.today)

    class Meta:
        unique_together = ['first_name', 'last_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(models.Model):
    title = models.CharField(max_length=150)
    isbn = models.CharField(max_length=13)
    published = models.DateField(default=datetime.date.today)
    pages = models.PositiveSmallIntegerField(default=0)
    author = models.ManyToManyField(Author, blank=True, related_name='books')

    def __str__(self):
        return self.title
