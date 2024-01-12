from django.db import models
from django.contrib.auth import get_user_model


class Readinglist(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    books = models.ManyToManyField('books.Book', blank=True)

    def __str__(self):
        return f"{self.owner}'s Reading List"
