from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo

class RestetPassword(FlaskForm):
    password = PasswordField('Password:',
        validators=[DataRequired(),Length(min=6,max=12)])
    passwordConfirm = PasswordField('Password confirmation:',
        validators=[DataRequired(),EqualTo('password')])
    
    submit = SubmitField('Set new password')