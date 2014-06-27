from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


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
