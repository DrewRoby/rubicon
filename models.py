from .app import db

class Player(db.Model):
    __tablename__ = 'player'

    playerid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    usertag = db.Column(db.String(64))

    def __repr__(self):
        return '<Player %r>' % (self.usertag)

class Game(db.Model):
    __tablename__ = 'game'

    gameid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    publisher = db.Column(db.String(64))
    numplayers = db.Column(db.Integer)
    sesslengthmin = db.Column(db.Integer)
    sesslengthmax = db.Column(db.Integer)
    genre = db.Column(db.String(64))
    gametype = db.Column(db.String(64))
    platform = db.Column(db.String(64))

    def __repr__(self):
        return '<Players %r>' % (self.nickname)

class Session(db.Model):
    __tablename__ = 'session'

    sessionid = db.Column(db.Integer, primary_key=True)
    gameid = db.Column(db.Integer, ForeignKey(game.gameid), nullable=False)
    gameid = db.Column(db.Integer, ForeignKey(game.gameid), nullable=False)
    gameid = db.Column(db.Integer, ForeignKey(game.gameid), nullable=False)
    
    usertag = db.Column(db.String(64))

class Con(db.Model):
    __tablename__ = 'con'

    conid = db.Column(db.Integer, primary_key=True)
    conname = db.Column(db.String(64))
    conbegin = db.Column(db.DateTime)