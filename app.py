# import necessary libraries
import os
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    send_from_directory
    )

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL','') or "sqlite:///db/db.sqlite"

# db = SQLAlchemy(app)



# @app.before_first_request
# def setup():
#     # Recreate database each time for demo
#     # db.drop_all()
#     db.create_all()

#TODO refactor for rubicon
# Get navbar to work... whither dropdown?[]
# Add routes for existing templates (or rather nav options)
@app.route("/")
def home():
    return render_template('home.html')

@app.route("/register")
def register():
    return render_template('register.html')

@app.route("/library")
def get_library():
    return render_template('library.html')

@app.route("/profile")
def get_profile():
    return render_template('profile.html')

@app.route("/cons")
def get_cons():
    return render_template('cons.html')

@app.route('/join')
def join_game():
    return render_template('gamenav.html')

@app.route("/gamenav", methods=["GET","POST"])
def add_game():
    if request.method == "POST":
        username = request.form['username']
        game = request.form['game']
        #should add game to user library (or to con?) if not available
        # redirect to game.html
    # Connection to db should be in js?
    # Any rate, want to insert new session for current con, user
    # allow invites
    return render_template('gamenav.html')

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


@app.route("/assets/<path:path>")
def send_asset(path):
    return send_from_directory('assets', path) 

if __name__ == "__main__":
    app.run(debug=True)
