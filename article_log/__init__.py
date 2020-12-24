from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os

flask_bcrypt = Bcrypt()
login_manager = LoginManager()

def create_app():
    global flask_bcrypt

    app = Flask(__name__)

    ## flask app 설정
    from article_log.config import ArticleLogConfig
    app.config.from_object(ArticleLogConfig)
    app.config.suppress_callback_exceptions = True
    app.env = 'development'

    login_manager.session_protection = 'strong'
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    ## Log 초기화
    from article_log.article_log_logger import Log
    log_filepath = os.path.join(app.root_path,
                                app.config['LOG_FILE_PATH'])
    Log.init(log_filepath=log_filepath)

    ## Session
    from article_log.cache_session import SimpleCacheSessionInterface
    app.session_interface = SimpleCacheSessionInterface()

    ## database 연결
    from article_log.model.database import DB
    db_filepath = os.path.join(app.root_path,
                               app.config['DB_FILE_PATH'])
    db_url = app.config['DB_URL'] + db_filepath
    DB.init(db_url, eval(app.config['DB_LOG_FLAG']))
    DB.init_db()

    ##flask_bcrypt password hash
    flask_bcrypt.init_app(app)

    ## Blueprint
    from article_log.controller import login_page,register, view_page

    from article_log.article_log_blueprint import article_log_blueprint

    app.register_blueprint(article_log_blueprint)

    return app


