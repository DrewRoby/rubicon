# Rubicon!

### A Simple Board Game Tracker
From organizing a your personal games library to organizing a weekend games conference, Rubicon! has you covered.  Or it will, anyhow: this is VERY MUCH in development.  Feel free to send in a PR if you want to pitch in.

#### Planned Functionality
1. Plan everything from a small game night with friends to a multi-day, multi-group marathon
1. Track play-time of games, including multiple rounds of the same game
3. Organize your own games library, and pool with friends to coordinate a game night
5. A dashboard that shows your library, sessions, win rates, favorite games, and bestest besties
2. Use [flaskbb](https://github.com/flaskbb/flaskbb) for communication, be it planning, logistics, rants, or trash talk


I plan to deploy this to a free Heroku instance and keep it up there, so feel free to use it for more than just Rubicon IV: Wrath of Con.  Theoretically it could work as well for LAN parties as it could for board games, but surely to focus on that would be to reinvent the wheel.


#### Current Worklist
* Get navbar in layout.html to work... whither dropdown? (update 2/2: it has something to do with the Popper library that Bootstrap uses.  It's weird.)
* Add routes to app.py for existing templates (or rather, existing nav options)
* Download postgres and link it up to the app on the backend.  Data model already exists in models.py.  
