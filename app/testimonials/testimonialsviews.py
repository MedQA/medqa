'''
   Testimonials
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)

#from app.user import User
from app.extensions import db
#from userforms import SignupForm, LoginForm, UserProfileForm, ForgotPasswordForm, ResetPasswordForm
#from flask_mail import Message

testimonials = Blueprint('testimonials', __name__,url_prefix='/<firstname>/testmonials')

@testimonials.route('/')
def home(firstname):
    return "Hi"
