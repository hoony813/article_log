from flask import render_template, request, redirect, session, current_app, flash
from flask_login import login_required, login_user, logout_user, current_user

from article_log.article_log_blueprint import article_log_blueprint
from article_log.model.forms import LoginForm
from article_log.model.database import dao
from article_log.article_log_logger import Log
from article_log.model.user import User
from article_log import flask_bcrypt, login_manager

@article_log_blueprint.teardown_request
def close_db_session(exception=None):
    ## 요청이 완료된 후에 db연결에 사용된 세션을 종료함
    try:
        dao.remove()
    except Exception as e:
        Log.error(str(e))

@article_log_blueprint.route("/", methods=['GET','POST'])
def login_page():
    session_key = request.cookies.get(current_app.config['SESSION_COOKIE_NAME'])
    if session.sid == session_key and session.__contains__('username'):
        return redirect('/article-view')

    form = LoginForm(request.form)
    if request.method == "POST":
        if form.validate():
            userObj = User()
            user = userObj.get_by_username(form.username.data)
            if user:
                if flask_bcrypt.check_password_hash(user.password, form.password.data):
                    if login_user(user):
                        session.permanent = True
                        session['username'] = user.username
                        return redirect('/article-view')
                    else:
                        flash('unable to loing in')
                else:
                    flash("Sorry incorrect username or password")
            else:
                flash("Sorry incorrect username or password")
    return render_template("login.html", form=form)

@login_manager.user_loader
def load_user(_id):
    temp = User()
    a = temp.get_by_id(_id)

    return a

@login_manager.unauthorized_handler
def unauthorized():
    flash("You must be logged in")
    return redirect('/')

@article_log_blueprint.route('/log-out',methods=['GET','POST'])
@login_required
def logout():
    logout_user()
    # session.pop('username')
    session.clear()
    flash('Logged out!')
    return redirect('/')