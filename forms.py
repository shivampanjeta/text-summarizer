from flask_wtf import FlaskForm
from wtforms.widgets import TextArea

from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LinkForm(FlaskForm):
    link = StringField('Link', [validators.Length(min=3, max=1000)])

    sum =  StringField('Sum', widget=TextArea())

    submit = SubmitField('Summarize')
