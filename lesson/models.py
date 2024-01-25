from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Game(models.Model):
    name = models.CharField(max_length=150)
    creation_year = models.IntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)

    genre = models.ManyToManyField(Genre, related_name="games")


    def __str__(self):
        return self.name