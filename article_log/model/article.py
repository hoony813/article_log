from sqlalchemy import Column, Integer, String

from article_log.model import Base
from article_log.model.database import dao

class Article(Base):

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, unique=False)
    article_title = Column(String, unique=False)
    article_url = Column(String, unique=False)
    article_src = Column(String, unique=False)
    article_description = Column(String, unique=False)
    comment = Column(String, unique=False)

    def __init__(self, user_id, article_title, article_url,article_src,article_description,comment):
        self.user_id = user_id
        self.article_title = article_title
        self.article_url = article_url
        self.article_src = article_src
        self.article_description = article_description
        self.comment = comment

    def __repr(self):
        return '<Article %r %r %r %r>' % (self.article_title, self.article_url, self.article_src, self.comment)