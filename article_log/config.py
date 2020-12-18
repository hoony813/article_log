import os

class ArticleLogConfig(object):
    TESTING = True
    DEBUG = True

    SECRET_KEY = os.urandom(24)

    DB_URL = 'sqlite:///'

    DB_FILE_PATH = 'resource/database/photolog'

    UPLOAD_FOLDER = 'resource/uplooad/'


