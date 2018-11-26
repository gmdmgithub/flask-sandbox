from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sandbox.models import User

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