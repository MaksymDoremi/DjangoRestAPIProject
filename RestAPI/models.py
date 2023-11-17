from django.db import models


class Author(models.Model):
    Username = models.CharField(max_length=64, unique=True)
    Password = models.CharField(max_length=64)
    Name = models.CharField(max_length=64)
    Surname = models.CharField(max_length=64)

class Blog(models.Model):
    Content = models.CharField(max_length=500)
    Date = models.DateField()
    Author = models.ForeignKey(Author, on_delete=models.PROTECT)
