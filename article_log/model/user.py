from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_login import UserMixin, AnonymousUserMixin

from article_log.model import Base
from article_log.model.database import dao

class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(50), unique=False)
    password = Column(String(50), unique=False)


    def __init__(self, username=None, email=None, password=None, auth=True):
        self.username = username
        self.email = email
        self.password = password
        self.auth = auth

    def __repr__(self):
        return '<User %r %r>' % (self.username, self.email)


    def get_by_username(self,username):
        user = dao.query(User).filter_by(username=username).first()

        if user:
            self.id = user.id
            self.username = user.username
            self.email = user.email
            self.password = user.password

            return self

        else:
            return None

    def get_by_id(self,id):
        user = dao.query(User).filter_by(id=id).first()

        if user:
            self.id = user.id
            self.username = user.username
            self.email = user.email
            self.password = user.password

            return self

        else:
            return None

    def is_auth(self):
        return self.auth

class Anonymous(AnonymousUserMixin):
    name = u"Anonymous"