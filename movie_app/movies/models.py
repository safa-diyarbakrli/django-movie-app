from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    description = models.TextField()
    picture = models.CharField(max_length=100)
    mainpage = models.BooleanField(default=False)
