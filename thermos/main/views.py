from flask import render_template

from . import app
from .. import login_manager
from ..models import User, Bookmark, Tag

@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(userid))

@app.route('/')
@app.route('/index')
def index():
     return render_template('index.html', new_bookmarks=Bookmark.newest(5))


#Error handling
@app.app_errorhandler(403)
def unauthorized(e):
    return render_template('403.html'), 403


@app.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.app_errorhandler(500)
def server_error(e):
    return render_template('500.html', error=e), 500

#Global additions
@app.app_context_processor
def inject_tags():
    return dict(all_tags=Tag.all)


