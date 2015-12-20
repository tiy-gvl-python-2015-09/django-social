from django.db import models
from django.views.generic import View


#https://roll20.net/

__author__ = 'MatthewBarnette'


class UserName(models.Model):

    def __str__(self):
        return self.username

    username = models.TextField(max_length=50)
    photo = models.ImageField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    follows = models.ManyToManyField('self', related_name='game_follows', symmetrical=False)
    subscription = models.TextField(max_length=15)

class Character(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=25)
    char_class = models.CharField(max_length=10)
    race = models.CharField(max_length=10)
    owner = models.ForeignKey(UserName)
    character_sheet = models.FileField()


class Game(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=30)
    photo = models.ImageField()
    playing = models.TextField(max_length=25)
    description = models.TextField(max_length=250)
    frequency = models.CharField(max_length=10)
    players_needed = models.IntegerField()
    game_type = models.CharField(max_length=10)
    language = models.CharField(max_length=25)
    audio_visual = models.CharField(max_length=15)
    new_players_welcome = models.BinaryField()
    mature_content = models.BinaryField()
    players = models.DictWrapper()
    owner = models.ForeignKey(UserName)


class Map(models.Model):

    def __str__(self):
        return self.name

    name = models.CharField(max_length=25)
    map = models.ImageField()
    owner = models.ForeignKey(UserName)