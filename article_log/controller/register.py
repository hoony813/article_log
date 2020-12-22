from flask import render_template, request, redirect

from article_log.article_log_blueprint import article_log_blueprint
from article_log.model.forms import RegistrationForm
from article_log.model.database import dao
from article_log.model.user import User
from article_log import flask_bcrypt


@article_log_blueprint.route('/register',methods=['GET','POST'])
def register_user_form():
    form = RegistrationForm(request.form)
    if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        try:
            user = User(username,
                        email,
                        flask_bcrypt.generate_password_hash(password))
            dao.add(user)
            dao.commit()

        except Exception as e:
            error = "DB error occurs : " + str(e)
            dao.rollback()
            print(error)
            raise e
        else:
            return redirect('/')

    return render_template('register.html', form=form)