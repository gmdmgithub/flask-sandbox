from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length

from flask_sandbox.models import Post



class NewPostForm(FlaskForm):
    title = StringField('User name:',validators=[
        DataRequired(),Length(min=5, max=100)
    ])
    content = StringField('Password:',validators=[
        DataRequired(),Length(min=1,max=2000)
    ])

    submit = SubmitField('Save post')