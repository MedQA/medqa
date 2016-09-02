from flask.ext.wtf import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, Email, EqualTo, Optional


class TestimonialsForm(Form):
    title = StringField('Title', validators=[Required(),Length(1,250)])
    description = TextAreaField('Description')
    submit = SubmitField('Submit')
