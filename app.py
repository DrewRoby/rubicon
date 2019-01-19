# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/db.sqlite"

db = SQLAlchemy(app)


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
    
@app.before_first_request
def setup():
    # Recreate database each time for demo
    db.drop_all()
    db.create_all()


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        nickname = request.form["nickname"]
        age = request.form["age"]

        pet = Pet(nickname=nickname, age=age)
        db.session.add(pet)
        db.session.commit()

        return "Thanks for the form data!"

    return render_template("form.html")


@app.route("/api/data")
def list_pets():
    results = db.session.query(Pet.nickname, Pet.age).all()

    pets = []
    for result in results:
        pets.append({
            "nickname": result[0],
            "age": result[1]
        })
    return jsonify(pets)


@app.route("/")
def home():
    return "Welcome!"


if __name__ == "__main__":
    app.run()
