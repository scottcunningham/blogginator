import config
import hashlib
import sqlalchemy

from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from sqlalchemy.orm import sessionmaker
from populate_db import Post, populate_db


# Import configuration
DATABASE = config.DATABASE_FILE
DEBUG = config.DEBUG
SECRET_KEY = config.SECRET_KEY

# Boiler-plate
app = Flask(__name__)
app.config.from_object(__name__)


def hash_password(password):
    return hashlib.sha512(password).hexdigest()


def check_login(username, password):
    user = g.session.query(Post).filter_by(username=username).first()

    if not user:
        return False

    if user.password == hash_password(password):
        return True
    else:
        return False


def connect_db():
    return sqlite3.connect(app.config['DATABASE'])


def init_db():
    populate_db(app.config['DATABASE'])


@app.before_request
def before_request():
    g.engine = sqlalchemy.create_engine("sqlite:///{}".format(app.config['DATABASE']))
    g.Session = sessionmaker(bind=g.engine)
    g.session = g.Session()


@app.teardown_request
def teardown_request(exception):
    pass


@app.route('/', methods=['GET'])
def show_entries():
    posts = g.session.query(Post)
    print posts
    #return render_template('show_entries.html', entries=entries)
    return render_template('index.html', entries=posts)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    title, content = request.form['title'], request.form['text']

    insert = g.posts.insert()
    insert.execute(date=int(time.time()), title=title, content=content)

    return redirect(url_for('show_entries'))


@app.route('/posts/<post_id>', methods=['GET'])
def show_post(post_id):

    post = g.session.query(Post).filter_by(post_id=post_id).first()

    if not post:
        abort(404)

    return render_template('post.html', post_id=post.post_id, title=post.title, text=post.content)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print request.form['username'], request.form['password']
        if not (check_login(request.form['username'],
                request.form['password'])):
            error = 'Invalid username or password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(use_debugger=True, debug=True)
