Based on the pluralsight course: Introduction to the Flask Microframework

Built using the flaskapp conda env.
    $ activate flaskapp
============================
For generating a secret_key for the session, try this from the console:
    $ python
    >> import os
    >> os.urandom(24)  
or something of the like...
============================

Working with the db
    #committing queries
    >> from thermos import db
    >> from models import User, Bookmark
    >> db.create_all() #creates a thermos.db file
    >> u=User(username="something",email="test@example.com")
    >> db.session.add(u)  #stages the data in u for commit to the db
    >> db.session.commit() #commits the data to the db
    
    >> from datetime import datetime
    >> db.session.add(Bookmark(url="http://www.somewhere.com", date=datetime.utcnow(), description="This should take you somewhere"))
    >> db.session.commit()
    #Getting information from the db
    >> User.query.get(1) # gets the User with an id of 1
    >> User.query.filter_by(username="CrashBandicoot").all() #gets all of the records where username=CrashBandicoot
    
    >> u = User.query.get(1)
    >> u.bookmarks.all() #select * from Bookmarks where user_id = 1
    >> u.bookmarks[1].user #show the username for the second bookmark
================================

Database version control
==========================
the db variable is set in the manage.py file
    #show a list of available commands
    >> python manage.py db
    
    #initialize the db
    >> python manage.py db init
    
    #create an initial migration with the message tag 'initial'
    >> python manage.py db migrate -m "initial"
    
    #In order to get the the latest version migrated
    #run the upgrade command(check migrations/versions/randomnumber_initial.py)
    >> python manage.py db upgrade
    
    #To fall back on a previous version
    >> python manage.py db downgrade
    
    #To fall backto a specific version(here the version with the 'initial' tag):
    >> python manage.py db downgrade --tag initial
    
    #To upgrade to a specific version(here the version with the 'tags' tag):
    >> python manage.py db upgrade --tag tags
    
    
    
=================================
=== Requirements ===

flask-migrate
flask-moment
