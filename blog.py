import sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import hashlib

# configuration
DATABASE = 'db.db'
DEBUG = True
SECRET_KEY = 'development key'

app = Flask(__name__)
app.config.from_object(__name__)

def hash_password(password):
    return hashlib.sha512(password).hexdigest()

def check_login(username, password):
    (username, real_password) = query_db("select * from users where username=='" + username + "'")[0]
    password_hash = hash_password(password)
    if real_password == password_hash:
        return True
    else:
        return False

def query_db(query):
    cur = g.db.execute(query)
    return cur.fetchall()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/', methods=['GET'])
def show_entries():
    cur = g.db.execute('select id, title, text from entries order by id desc')
    entries = [dict(title=row[1], text=row[2], idno=row[0]) for row in cur.fetchall()]
    print entries
    #return render_template('show_entries.html', entries=entries)
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/posts/<idno>', methods=['GET'])
def show_post(idno):
    post = query_db('select * from entries where id=' + idno)[0]
    return render_template('post.html', idno=idno, title=post[1], text=post[2])

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        print request.form['username'], request.form['password']
        if not (check_login(request.form['username'], request.form['password'])):
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
