from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from time import time


DEFAULT_DB_NAME = "db.db"

Base = declarative_base()


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
    session.commit()


if __name__ == '__main__':
    populate_db(DEFAULT_DB_NAME)
