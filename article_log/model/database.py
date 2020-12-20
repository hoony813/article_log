from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

class DB:

    __engine = None
    __session = None

    @staticmethod
    def init(db_url, db_log_flag=True):
        DB.__engine = create_engine(db_url, echo=db_log_flag)
        DB.__session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=DB.__engine))

        global dao
        dao = DB.__session

    @staticmethod
    def init_db():
        from article_log.model import user

        from article_log.model import Base
        Base.metadata.creae_all(bind=DB.__engine)


dao = None
