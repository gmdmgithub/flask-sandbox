from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length

from flask_sandbox.models import Post



class EditPostForm(FlaskForm):
    title = StringField('Title:',
        validators=[DataRequired(),Length(min=5, max=100)]
    )
    content = TextAreaField('Content:',
        validators=[DataRequired(), Length(min=1,max=2000)],
        description={'style': 'font-size: 1rem'}
    )

    submit = SubmitField('Save post')