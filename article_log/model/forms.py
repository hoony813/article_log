from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, Form
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, ValidationError, Optional, EqualTo, InputRequired

class LoginForm(Form):
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired()])

class RegistrationForm(Form):
    email = EmailField('email', [InputRequired()])
    username = StringField('Username', [InputRequired()])
    password = PasswordField('Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')