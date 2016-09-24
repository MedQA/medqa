from flask_wtf import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
from wtforms.validators import Required, Length, Email, EqualTo, Optional


class TestimonialsForm(Form):
    title = StringField('Title', validators=[Required(),Length(1,250)])
    description = TextAreaField('Description',validators=[Required(),Length(1,1000)])
    submit = SubmitField('Submit')
