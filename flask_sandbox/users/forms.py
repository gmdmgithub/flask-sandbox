from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError, BooleanField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sandbox.models import User
from flask_login import current_user


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


class LoginForm(FlaskForm):
    username = StringField('User name:',validators=[
        DataRequired(),Length(min=5, max=20)
    ])
    password = PasswordField('Password:',validators=[
        DataRequired(),Length(min=5,max=12)
    ])
    rememberMe = BooleanField('Remember me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username:',
        validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email:', 
        validators=[Email(),DataRequired()])
    image = FileField('Update profile picture',
        validators=[FileAllowed(['jpg','jpeg','png'])])

    submit = SubmitField('Update')
    
    def validate_username(self,username):
        if username.data !=  current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValueError('Username already exists. Please choose a different one')

    def validate_email(self,email):
        if email.data !=  current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValueError('Something wrog with your data')

class RestetPassword(FlaskForm):
    password = PasswordField('Password:',
        validators=[DataRequired(),Length(min=6,max=12)])
    passwordConfirm = PasswordField('Password confirmation:',
        validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Set new password')


class ResetRequestForm(FlaskForm):
    email = StringField('Email:', validators=[Email(),DataRequired()])
    submit = SubmitField('Send request')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValueError('Something wrog with your data')