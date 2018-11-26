from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length

from flask_sandbox.models import User

class LoginForm(FlaskForm):
    username = StringField('User name:',validators=[
        DataRequired(),Length(min=5, max=20)
    ])
    password = PasswordField('Password:',validators=[
        DataRequired(),Length(min=5,max=12)
    ])
    rememberMe = BooleanField('Remember me')
    submit = SubmitField('Login')