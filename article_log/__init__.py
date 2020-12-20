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

    from article_log.controller import login_page

    from article_log.article_log_blueprint import article_log_blueprint

    app.register_blueprint(article_log_blueprint)

    return app


