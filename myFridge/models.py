from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    username = models.CharField(max_length=25, unique=True)
    email = models.EmailField(max_length=50, unique=True)
    #password = models.CharField(max_length = 50)
    #icon_URL = models.ImageField()
    active = models.BooleanField(default=True)
    member_since = models.DateTimeField(auto_now_add=True)
    is_superuser = models.BooleanField(default=False)
    #ingredients = models.ManyToManyField(Ingredient)
    #
    def __str__(self):
        return self.username


class Ingredient(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.name
