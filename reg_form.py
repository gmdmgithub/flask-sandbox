from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username:',
        validators=[DataRequired(), Length(min=5, max=20)],
        render_kw={"placeholder": "set a username"})
    password = PasswordField('Password:',
        validators=[DataRequired(),Length(min=6,max=12)])
    passwordConfirm = PasswordField('Password confirmation:',
        validators=[DataRequired(),EqualTo(password)])
    email = StringField('Email:', 
        validators=[Email(),DataRequired()])
    
    submit = SubmitField('Sign Up')