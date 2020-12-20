from flask import render_template, request

from article_log.article_log_blueprint import article_log_blueprint
from article_log.model.forms import LoginForm
from article_log.model.database import dao
from article_log.model.user import User

@article_log_blueprint.route("/", methods=['GET','Method'])
def login_page():
    form = LoginForm(request.form)

    return render_template("login.html", form=form)