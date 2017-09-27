from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=128)

    def __str__(self):
        return "{0.author}'s \"{0.name}\"".format(self)

