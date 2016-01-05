from thermos import app, db
from thermos.models import User, Bookmark
from flask.ext.script import Manager, prompt_bool
from flask.ext.migrate import Migrate, MigrateCommand

manager = Manager(app)
migrate = Migrate(app,db)
#gives acccess to db migration commands
manager.add_command('db', MigrateCommand)

@manager.command
def initdb():
    db.create_all()
    print 'Initialized the database'
    
    
def seedBookmarks():
    u = User.query.get(1)
    for bm in ["test1", "test2", "test3"]:
        db.session.add(Bookmark(user=u, url=bm))
    v = User.query.get(2)
    for bm in ["test4", "test5"]:
        db.session.add(Bookmark(user=v, url=bm))
    db.session.commit()
    print 'Seeded Bookmarks'
    
@manager.command
def seedUsers():
    db.session.add(User(username="BillyBob", email="bbob@bbop.com", password="test"))
    db.session.add(User(username="CrashBandicoot", email="Bandicoot@rush.com", password="test"))
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
