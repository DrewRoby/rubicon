# Rubicon!

### A Simple Board Game Session Tracker
From organizing a your personal games library to organizing a weekend games conference, Rubicon! has you covered.  Or it will, anyhow: this is VERY MUCH in development.  Feel free to send in a PR if you want to pitch in.

#### Planned Functionality
1. Plan everything from a small game night with friends to a multi-day, multi-group marathon
1. Track play-time of games, including multiple rounds of the same game
3. Organize your own games library, and pool with friends to coordinate a game night
5. A dashboard that shows your library, sessions, win rates, favorite games, and bestest besties
2. Use [flaskbb](https://github.com/flaskbb/flaskbb) for communication, be it planning, logistics, rants, or trash talk

<br>
I plan to deploy this to a free Heroku instance and keep it up there, so feel free to use it for more than just Rubicon IV: Wrath of Con.  Theoretically it could work as well for LAN parties as it could for board games, but surely to focus on that would be to reinvent the wheel.


### Current Worklist
#### Latest Changes
* 2/20 refactor into properly named apps (e.g. session vs rubicon_app)
* Error when running createsuperuser: `AttributeError: 'AdminSite' object has no attribute 'Register'`

#### High Priority
* Support multiple users. / route needs to land at login page and/or check for logged-in cookie.  Implementing with some help from this [Very helpful resource](https://www.youtube.com/watch?v=D6esTdOLXh4).
* Work through process of adding or joining a game
* Profile form
* New con form
* /gamenav route needs to work for adding or joining.  Or just need to refactor into 2 different methods for adding a new game session vs. joining a game in progress.
* Library mgmt routes

#### Medium Priority
* Wire up postgres to the app on the backend.  Data model exists in models.py. 
* Add quote log

#### Low Priority
* Redesign data model around [RedisGraph](https://oss.redislabs.com/redisgraph/) or some other graph db? You know, for kicks?

#### Complete
* Replace bootstrap with bulma
* Add routes to app.py for existing templates (or rather, existing nav options)
* /gamenav as implemented should be /seshnav

#### Why?
I had a long weekend of gaming with some friends, and along with standard coordination issues (who's bringing what game? What's our agenda?), I was interested in seeing metrics on what everyone thought of the games they played, how long they played them, how many sessions, &c.  "Well," I thought, "I know how to fix this..."

#### Dev Setup
* SQLite DB does not persist from session to session, so:
* Run `python manage.py makemigrations`
* Run `python manage.py migrate`
* Run `python manage.py createsuperuser --name='ChosenOne' --email='PartyingWithAnimals@TheDesert.com'`
* The /admin route will now work properly.  Log in, hang out, blow your mind, have yourself a gas.