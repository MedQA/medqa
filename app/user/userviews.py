'''
   Users API for Login and Signup
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask.ext.login import login_required, login_user, current_user,\
                            logout_user
from app.user import User
from app.extensions import db, login_manager
from userforms import SignupForm, LoginForm, UserProfileForm

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
        user.dob = request.form.get('date')
        if user.dob:
            form1.populate_obj(user)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('user.userprofile',firstname=user.firstname))
        return render_template('user/index.html', form1=form1, form2=form2, error='error')
    return render_template('user/index.html', form1=form1, form2=form2)

@user.route('/login/',methods=['GET','POST'])
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

@user.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('user.signup'))

@user.route('/<firstname>/')
@login_required
def userprofile(firstname):
    return render_template('user/userprofile.html', firstname=firstname)

@user.route('/<firstname>/edit_userprofile/',methods=['GET','POST'])
@login_required
def edit_userprofile(firstname):
    form = UserProfileForm()
    if form.validate_on_submit():
        """
        current_user.firstname = request.form.get('firstname')
        current_user.surname = request.form.get('surname')
        current_user.email = request.form.get('email')
        current_user.phone_number = request.form.get('phone_number')
        current_user.gender = request.form.get('gender')
        current_user.blood_grp = request.form.get('blood_grp')
        current_user.location = request.form.get('location')
        current_user.allergies = request.form.get('allergies')
        current_user.medical_ailments = request.form.get('medical_ailments')
        current_user.previous_medications = request.form.get('previous_medications')
        """
        user = current_user._get_current_object()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.userprofile', firstname=current_user.firstname))

    form.firstname.data = current_user.firstname
    form.surname.data = current_user.surname
    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    #form.gender.data = current_user.gender
    form.blood_grp.data = current_user.blood_grp
    form.location.data = current_user.location
    form.allergies.data = current_user.allergies
    form.medical_ailments.data = current_user.medical_ailments
    form.previous_medications.data =current_user.previous_medications
    return render_template('user/edit_userprofile.html', firstname=firstname, form=form)
