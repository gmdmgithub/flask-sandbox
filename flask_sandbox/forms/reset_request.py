from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_sandbox.models import User

class ResetRequestForm(FlaskForm):
    email = StringField('Email:', validators=[Email(),DataRequired()])
    submit = SubmitField('Send request')

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValueError('Something wrog with your data')