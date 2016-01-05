from thermos import app, db
from thermos.models import User, Bookmark, Tag
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)
#gives acccess to db migration commands
manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    
    BillyBob = User(username="BillyBob", email="bbob@bbop.com", password="test")
    Crash = User(username="CrashBandicoot", email="Bandicoot@rush.com", password="test")
    db.session.add(BillyBob)
    db.session.add(Crash)
    
    def add_bookmark(url, description, tags):
        db.session.add(Bookmark(url=url, description=description, user=Crash, tags=tags))
        
    for name in ['python', 'flask', 'webdev', 'programming', 'training', 'news', 'orm']:
        db.session.add(Tag(name=name))
    db.session.commit()
    

    add_bookmark('http://jimbo.com', "Jimbo, another web development site", "webdev,orm,python")
    add_bookmark('http://blank.com', "Blank, another web development site", "flask")
    add_bookmark('http://nothing.com', "A site about nothing", "python")
    add_bookmark('http://praxis.com', "A site with the name of a sweet band", "python,news")
    add_bookmark('http://mastodon.com', "A site with the name of another sweet band", "programming")
    add_bookmark('http://news.google.com', "Google News", "news")
    add_bookmark('http://realpython.com', "Python training site", "programming,python")
    add_bookmark('http://beef.com', "Its where the beef is", "news")
    db.session.commit()
    
@manager.command
def seedUsers():
    db.session.commit()
    seedBookmarks()
    print 'Seeded Users/Bookmarks'
    
@manager.command
def dropdb():
    if prompt_bool(
        "Are you sure you want to drop all of your data?"):
        db.drop_all()
        print "Dropped the database"
    
if __name__ == '__main__':
    manager.run()
