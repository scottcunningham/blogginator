from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from time import time
from hashlib import sha1

from model.user import User
from model.post import Post


DEFAULT_DB_NAME = "db.db"


def populate_db(filename):
    engine = create_engine("sqlite:///{}".format(filename), echo=True)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    default_post = Post(post_id=0, date=int(time()), title="Hello World",
            content="Welcome :)")
    session.add(default_post)

    user = User(user_id=0, username='root', real_name='Root Fairy',
            password_hash=sha1('password').hexdigest())
    session.add(user)

    session.commit()


if __name__ == '__main__':
    populate_db(DEFAULT_DB_NAME)
