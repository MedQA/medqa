'''
   Users API for Login and Signup
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask.ext.login import login_required, login_user, current_user,\
                            logout_user
from app.user import User
from app.extensions import db, login_manager, mail
from userforms import SignupForm, LoginForm, UserProfileForm, ForgotPasswordForm, ResetPasswordForm
from flask_mail import Message

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
        user = current_user._get_current_object()
        form.populate_obj(user)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user.userprofile', firstname=current_user.firstname))

    form.firstname.data = current_user.firstname
    form.surname.data = current_user.surname
    form.email.data = current_user.email
    form.phone_number.data = current_user.phone_number
    form.blood_grp.data = current_user.blood_grp
    form.location.data = current_user.location
    form.allergies.data = current_user.allergies
    form.medical_ailments.data = current_user.medical_ailments
    form.previous_medications.data =current_user.previous_medications
    return render_template('user/edit_userprofile.html', firstname=firstname, form=form)

@user.route('/forgot_password', methods=['GET','POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        email = form.email.data
        user = User.query.filter_by(email=email).first()

        if user:
            token = user.get_token()
            msg = Message('PasswordReset[MedQa]', sender = 'garg95hitesh@gmail.com', recipients=[user.email])
            msg.body = "You're receiving this email because you requested a password reset for your user account at Medqa.in\n\n Please go to the following page and choose a new password:\n http://0.0.0.0:5000/reset_password?token=" + token+ "\n\nThanks!\nTeam Medqa"
            mail.send(msg)
            return "sent"
        else:
            error = "Email Address Not Registered!"
            print error
            return render_template('user/forgot_password.html',form=form)
    return render_template('user/forgot_password.html',form=form)

@user.route('/reset_password', methods=['GET','POST'])
def reset_password():
    token = request.args.get('token',None)
    verifed_result = User.verify_token(token)
    if token and verifed_result:
        form = ResetPasswordForm()
        if form.validate_on_submit():
            password = form.password.data
            verifed_result.password = password
            db.session.add(verifed_result)
            db.session.commit()
            return redirect('user.login')
        return render_template('user/reset_password.html',form=form)
    return "Token expired"
