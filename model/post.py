from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


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
