import os

class ArticleLogConfig(object):
    TESTING = True
    DEBUG = True

    SECRET_KEY = os.urandom(24)

    DB_URL = 'sqlite:///'

    DB_FILE_PATH = 'resource/database/photolog'

    UPLOAD_FOLDER = 'resource/uplooad/'

    DB_LOG_FLAG = 'True'

    LOG_LEVEL = 'debug'

    LOG_FILE_PATH = 'resource/log/articlelog.log'

    SESSION_COOKIE_NAME = 'article_log'

    PERMANENT_SESSION_LIFTIME = 60*60*2

