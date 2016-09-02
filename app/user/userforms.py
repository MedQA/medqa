from flask.ext.wtf import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextField
from wtforms.validators import Required, Length, Email, EqualTo, Optional
from .usermodels import User

class SignupForm(Form):
    firstname = StringField('Firstname', validators=[Required(),Length(1,70)])
    surname = StringField('Lastname',validators=[Required(),Length(1,70)])
    email = StringField('Email', validators=[Required(), Length(1,70), Email()])
    password = PasswordField('Password', validators=[Required()])
    confirm_Password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password', message='Passwords must match')])
    phone_number = StringField('Phone Number',validators=[Required(),Length(9,10)])
    #bday_date = IntegerField('Date', validators=[Required()]])
    #bday_month = StringField('Month',validators=[Required()]])
    #bday_year = IntegerField('Year', validators=[Required()]])
    gender = StringField(validators=[Required()])
    terms_cond = BooleanField(validators=[Required()])
    submit = SubmitField('Signup')

class LoginForm(Form):
    useremail = StringField('Email',validators=[Required(),Length(1,70),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember_me = BooleanField(default=False)
    submit = SubmitField()

class UserProfileForm(Form):
    firstname = StringField('Firstname', validators=[Required(),Length(1,70)])
    surname = StringField('Lastname',validators=[Required(),Length(1,70)])
    email = StringField('Email', validators=[Required(), Length(1,70), Email()])
    phone_number = StringField('Phone Number',validators=[Optional(),Length(9,10)])
    #gender = StringField(validators=[Optional()])
    #dob = StringField(validators=[Optional()])
    blood_grp = StringField(validators=[Optional()])
    location = StringField(validators=[Optional()])
    allergies = StringField(validators=[Optional()])
    medical_ailments = StringField(validators=[Optional()])
    previous_medications = StringField(validators=[Optional()])
    submit = SubmitField('Update')


class ForgotPasswordForm(Form):
    email = StringField('Email', validators=[Required(), Length(1,70), Email()])

class ResetPasswordForm(Form):
    password = PasswordField('Password', validators=[Required()])
    confirm_Password = PasswordField('Confirm Password',validators=[Required(),EqualTo('password', message='Passwords must match')])
