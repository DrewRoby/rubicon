# Describes the data model of the application in SQL
# from .app import db
from django.db import models

class Player(db.Model):
    __tablename__ = 'PLAYER'

    PLAYER_ID = db.Column(db.Integer, primary_key=True)
    PLAYER_NAME = db.Column(db.String(64))
    PLAYER_USER_TAG = db.Column(db.String(64))
    EMAIL = db.Column(db.String(64))
    REGISTER_DATE = db.Column(db.DateTime) #set default value to current ts?

    def __str__(self):
        return self.usertag


class Player_Group(db.Model):
    __tablename__ = 'PLAYER_GROUP'

    PLAYER_P_GROUP_ID = db.Column(db.Integer, primary_key=True)
    PLAYER_ID = db.Column(db.Integer, ForeignKey(PLAYER.PLAYER_ID), nullable = False)
    P_GROUP_ID = db.Column(db.Integer)



class Game(db.Model):
    __tablename__ = 'GAME'

    GAME_ID = db.Column(db.Integer, primary_key=True)
    GAME_NAME = db.Column(db.String(64))
    PUBLISHER = db.Column(db.String(64))
    NUM_PLAYERS = db.Column(db.Integer)
    GAME_LEN_MIN = db.Column(db.Integer)
    GAME_LEN_MAX = db.Column(db.Integer)
    GENRE = db.Column(db.String(64))
    GAME_TYPE = db.Column(db.String(64))
    PLATFORM = db.Column(db.String(64))

    def __str__(self):
        return self.GAME_NAME

class Con(db.Model):
    __tablename__ = 'CON'

    CON_ID = db.Column(db.Integer, primary_key=True)
    CON_NAME = db.Column(db.String(64))
    CON_OWNER = db.Column(db.Integer, ForeignKey(PLAYER.PLAYER_ID), nullable=False)
    CON_P_GROUP_ID = db.Column(db.Integer, nullable=False) #COMPOSITE KEY OF CON_ID AND P_GROUP_ID
    CON_BEGIN = db.Column(db.DateTime)
    CON_END = db.Column(db.DateTime)

    def __str__(self):
        return self.CON_NAME

class Session(db.Model):
    __tablename__ = 'SESSION'

    SESSION_ID = db.Column(db.Integer, primary_key=True)
    GAME_ID = db.Column(db.Integer, ForeignKey(GAME.GAME_ID), nullable=False)
    CON_ID = db.Column(db.Integer, ForeignKey(CON.CON_ID), nullable=False)
    P_GROUP_ID = db.Column(db.Integer)
    SESSION_BEGIN = db.Column(db.DateTime)
    SESSION_END = db.Column(db.DateTime)
    

class Round(db.Model):
    __tablename__ = 'ROUND'

    ROUND_ID = db.Column(db.Integer, primary_key=True)
    SESSION_ID = db.Column(db.Integer, ForeignKey(SESSION.SESSION_ID), nullable=False)
    ROUND_BEGIN = db.Column(db.DateTime)
    ROUND_END = db.Column(db.DateTime)