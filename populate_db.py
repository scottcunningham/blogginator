from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from time import time


DEFAULT_DB_NAME = "db.db"

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True)
    username = Column(String)
    real_name = Column(String)
    password_hash = Column(String)

    def __repr__(self):
        return "<User(user_id={}, username={}, real_name={}, password_hash={})" \
                .format(user_id, username, real_name, password_hash)


class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True)
    date = Column(Integer)
    title = Column(String)
    content = Column(String)

    def __repr__(self):
        return "<Post(post_id={}, date={}, title={}, content={}>)".format(
                post_id, date, title, content)


def populate_db(filename):
    engine = create_engine("sqlite:///{}".format(filename), echo=True)

    Session = sessionmaker()
    Session.configure(bind=engine)

    session = Session()

    default_post = Post(post_id=0, date=int(time()), title="Hello World",
            content="Welcome :)")
    session.add(default_post)

    user = User(user_id=0, username='root', real_name='Root Fairy',
            password_hash='c8fed00eb2e87f1cee8e90ebbe870c190ac3848c  -')
    session.add(user)

    session.commit()


if __name__ == '__main__':
    populate_db(DEFAULT_DB_NAME)
