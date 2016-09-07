'''
   Testimonials
'''
from flask import (Blueprint, render_template, current_app, request,
                   flash, url_for, redirect, session, abort, jsonify)
from flask_login import login_required, login_user, current_user,\
                            logout_user

#from app.user import User
from app.extensions import db
#from userforms import SignupForm, LoginForm, UserProfileForm, ForgotPasswordForm, ResetPasswordForm
#from flask_mail import Message
from testimonialsforms import TestimonialsForm
from testimonialsmodels import Testimonials

testimonials = Blueprint('testimonials', __name__,url_prefix='/<firstname>/testmonials')

@testimonials.route('/add_testimonial', methods=['GET', 'POST'])
@login_required
def add_testimonial(firstname):
    form = TestimonialsForm()
    if form.validate_on_submit():
        testimonial = Testimonials(title=form.title.data,
                                    description = form.description.data,
                                    author = current_user)
        db.session.add(testimonial)
        db.session.commit()
        flash('Testimonial Added Successfully!')
        return redirect(url_for('user.userprofile',firstname=firstname))
    return render_template('testimonials/add_testimonial.html',form=form)
