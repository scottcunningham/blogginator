import config
import hashlib
import sqlalchemy

from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
    abort, render_template, flash
from markdown import markdown
from sqlalchemy.orm import sessionmaker
from time import time

from model.user import User
from model.post import Post




# Boiler-plate
app = Flask(__name__)
app.config.from_object('config')


def hash_password(password):
    return hashlib.sha1(password).hexdigest()


def check_login(username, password):
    user = g.session.query(User).filter_by(username=username).first()

    if not user:
        return False

    if user.password_hash == hash_password(password):
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


@app.route('/', methods=['GET', 'POST'])
def show_entries():
    posts = g.session.query(Post).order_by(Post.date.desc())
    #return render_template('show_entries.html', entries=entries)
    return render_template('posts.html', entries=posts)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    html_content = markdown(request.form['content'])

    title = 'No title'
    if request.form['title'] is not "":
        title = request.form['title']

    post = Post(title=title, content=html_content, date=time())

    g.session.add(post)
    g.session.commit()

    flash("Added entry!")
    return redirect(url_for('show_entries'))


@app.route('/posts/<post_id>', methods=['GET'])
def show_post(post_id):

    post = g.session.query(Post).filter_by(post_id=post_id).first()

    if not post:
        abort(404)

    return render_template('post.html', post_id=post.post_id, title=post.title, text=post.content)


@app.route('/login', methods=['POST'])
def login():
    if (check_login(request.form['username'],
            request.form['password'])):
        session['logged_in'] = True
        flash('You were logged in')
    else:
        flash('Error: Invalid username or password')

    return redirect(url_for('show_entries'))


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run(use_debugger=True, debug=True)
