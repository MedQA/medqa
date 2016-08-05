from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import Required, Length, Email, EqualTo

class SignupForm(Form):
    firstname = StringField('Firstname', validators=[Required(),Length(1,70)])
    surname = StringField('Lastname',validators=None)
    email = StringField('Email', validators=[Required(), Length(1,70), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_Password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password', message='Passwords must match')])
    phone_number = StringField('Phone Number',validators=[Required(),Length(10,12)])
    #bday_date = IntegerField('Date', validators=[Required()]])
    #bday_month = StringField('Month',validators=[Required()]])
    #bday_year = IntegerField('Year', validators=[Required()]])
    #gender = StringField(validators=[Required()]])
    terms_cond = BooleanField(validators=[Required()])
    submit = SubmitField('Log In')

class LoginForm(Form):
    email = StringField('Email',validators=[Required(),Length(1,70),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField(default=False)
    submit = SubmitField()
