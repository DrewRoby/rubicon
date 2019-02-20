from django.db import models
from datetime import datetime

# Create your models here.
class Player(models.Model):
    PLAYER_ID = models.AutoField(primary_key=True)
    PLAYER_NAME = models.CharField
    PLAYER_USER_TAG = models.CharField
    EMAIL = models.CharField
    REGISTER_DATE = models.DateTimeField(default=datetime.now, blank=True)

    # def __str__(self):
    #     return self.usertag
    # ^ Do I need these? ^


class Player_Group(models.Model):
    PLAYER_P_GROUP_ID = models.AutoField(primary_key=True)
    PLAYER_ID = models.ForeignKey(Player, on_delete=models.PROTECT)
    P_GROUP_ID = models.IntegerField



class Game(models.Model):
    GAME_ID = models.AutoField(primary_key=True)
    GAME_NAME = models.CharField
    PUBLISHER = models.CharField
    NUM_PLAYERS = models.IntegerField
    GAME_LEN_MIN = models.IntegerField
    GAME_LEN_MAX = models.IntegerField
    GENRE = models.CharField
    GAME_TYPE = models.CharField
    PLATFORM = models.CharField

    # def __str__(self):
    #     return self.GAME_NAME

class Con(models.Model):
    CON_ID = models.AutoField(primary_key=True)
    CON_NAME = models.CharField
    CON_OWNER = models.ForeignKey(Player, on_delete=models.PROTECT)
    CON_P_GROUP_ID = models.IntegerField #COMPOSITE KEY OF CON_ID AND P_GROUP_ID
    CON_BEGIN = models.DateTimeField
    CON_END = models.DateTimeField

    # def __str__(self):
    #     return self.CON_NAME

class Session(models.Model):
    SESSION_ID = models.AutoField(primary_key=True)
    GAME_ID = models.ForeignKey(Game, on_delete=models.PROTECT)
    CON_ID = models.ForeignKey(Con, on_delete=models.CASCADE)
    P_GROUP_ID = models.IntegerField
    SESSION_BEGIN = models.DateTimeField(default=datetime.now, blank=True)
    SESSION_END = models.DateTimeField
    

class Round(models.Model):
    ROUND_ID = models.AutoField(primary_key=True)
    SESSION_ID = models.ForeignKey(Session, on_delete=models.CASCADE)
    ROUND_BEGIN = models.DateTimeField(default=datetime.now, blank=True)
    ROUND_END = models.DateTimeField