from flask_wtf import FlaskForm
from wtforms import BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired
from wtforms import PasswordField, SubmitField


class LoginForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')
