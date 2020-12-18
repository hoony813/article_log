from flask import Flask
from flask_bcrypt import Bcrypt

def create_app():
    app = Flask(__name__)

    from article_log.config import ArticleLogConfig
    app.config.from_object(ArticleLogConfig)
    app.config.suppress_callback_exceptions = True
    app.env = 'development'

    flask_bcrypt = Bcrypt()
    flask_bcrypt.init_app(app)


