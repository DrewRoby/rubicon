# Rubicon!

### A Simple Board Game Session Tracker
From organizing a your personal games library to organizing a weekend games conference, Rubicon! has you covered.  Or it will, anyhow: this is VERY MUCH in development.  Feel free to send in a PR if you want to pitch in.

#### Planned Functionality
1. Plan everything from a small game night with friends to a multi-day, multi-group marathon
1. Track play-time of games, including multiple rounds of the same game
3. Organize your own games library, and pool with friends to coordinate a game night
5. A dashboard that shows your library, sessions, win rates, favorite games, and bestest besties
2. Use [Spirit](https://github.com/nitely/Spirit) for communication, be it planning, logistics, rants, or trash talk

<br>
I plan to deploy this to a free Heroku instance and keep it up there, so feel free to use it for more than just Rubicon IV: Wrath of Con.  Theoretically it could work as well for LAN parties as it could for board games, but surely to focus on that would be to reinvent the wheel.


### Current Worklist
[Project Plan](https://docs.google.com/document/d/1iyQvx6h56K4sixF306oxCg2OV1IbUly9dNVizWtOdDg/edit?usp=sharing)
#### Latest Changes
* 4/15 Application supports multiple users. Postgres now official database.

#### High Priority
* Figure out user dashboard: adding games to library, past/upcoming cons, &c.
* Work through process of adding or joining a game
* New con form

#### Medium Priority
* Straighten out the whole forum business
* Uh... [breadcrumbs](https://stackoverflow.com/questions/826889/how-to-implement-breadcrumbs-in-a-django-template) I guess

#### Low Priority
* Redesign data model around [RedisGraph](https://oss.redislabs.com/redisgraph/) or some other graph db? You know, for kicks?

#### Complete
* Replace bootstrap with bulma
* Add routes to app.py for existing templates (or rather, existing nav options)
* Wire up postgres
* Add login/logout

#### Why?
I had a long weekend of gaming with some friends, and along with standard coordination issues (who's bringing what game? What's our agenda?), I was interested in seeing metrics on what everyone thought of the games they played, how long they played them, how many sessions, &c.  "Well," I thought, "I know how to fix this..."

#### Dev Setup
* SQLite DB does not persist from session to session, so:
* Run `python manage.py makemigrations`
* Run `python manage.py migrate`
* Run `python manage.py createsuperuser --name='ChosenOne' --email='PartyingWithAnimals@TheDesert.com'`
* The /admin route will now work properly.  Log in, hang out, blow your mind, have yourself a gas.