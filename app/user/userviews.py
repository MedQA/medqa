'''
   Users API for Login and Signup
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask.ext.login import login_required, login_user, current_user,\
                            logout_user
from app.user import User
from app.extensions import db, login_manager
from userforms import SignupForm, LoginForm

user = Blueprint('user', __name__)

#@user.route('/')
@user.route('/', methods=['GET', 'POST'])
def signup():
    form1 = SignupForm()
    form2 = LoginForm()
    if form1.validate_on_submit():
        if User.is_email_taken(form1.email.data):
            return render_template('user/index.html', form1=form1,form2=form2, error = 'Email Address Already Taken!' )
        user = User()
        form1.populate_obj(user)

        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('user.userprofile',firstname=user.firstname))
    return render_template('user/index.html', form1=form1, form2=form2)

@user.route('/login',methods=['GET','POST'])
def login():
    form1 = SignupForm()
    form2 = LoginForm()
    if form2.validate_on_submit():
        user , authenticated = User.authenticate(form2.useremail.data,form2.password.data)
        if not authenticated:
            return render_template('user/index.html',form1=form1, form2=form2,usererror='Invalid email or password.')
        login_user(user, form2.remember_me.data)
        return redirect(url_for('user.userprofile',firstname=user.firstname))
    return render_template('user/index.html',form1=form1, form2=form2)

@user.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.signup'))

@user.route('/user/<firstname>')
@login_required
def userprofile(firstname):
    return render_template('user/userprofile.html', firstname=firstname)
