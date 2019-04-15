from django.db import models

class Game(models.Model):

    GAME_ID = models.IntegerField()
    GAME_NAME = models.CharField(max_length=200)
    PUBLISHER = models.CharField(max_length=200)
    NUM_PLAYERS = models.IntegerField
    GAME_LEN_MIN = models.IntegerField
    GAME_LEN_MAX = models.IntegerField
    GENRE = models.CharField(max_length=200)
    # GAME_TYPE = models.CharField(max_length=200)
    # PLATFORM = models.CharField(max_length=200)
