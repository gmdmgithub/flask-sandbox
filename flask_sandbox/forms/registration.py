from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sandbox.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username:',
        validators=[DataRequired(), Length(min=5, max=20)],
        render_kw={"placeholder": "set a username"})
    password = PasswordField('Password:',
        validators=[DataRequired(),Length(min=6,max=12)])
    passwordConfirm = PasswordField('Password confirmation:',
        validators=[DataRequired(),EqualTo('password')])
    email = StringField('Email:', 
        validators=[Email(),DataRequired()])
    
    submit = SubmitField('Sign Up')

    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValueError('Username already exists. Please choose a different one')
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValueError('Something wrog with your data')