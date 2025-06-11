from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Ім\'я користувача', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторіть пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструватися')