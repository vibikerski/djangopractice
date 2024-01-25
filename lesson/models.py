from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    birthday = models.DateField()
