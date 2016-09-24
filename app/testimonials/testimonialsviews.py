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

@testimonials.route('/<tid>/edit_testimonial', methods=['GET','POST'])
@login_required
def edit_testimonial(firstname, tid):
    form = TestimonialsForm()
    testimonial = Testimonials.query.filter_by(id=tid).first_or_404()
    if form.validate_on_submit():
        testimonial.title = form.title.data
        testimonial.description = form.description.data
        db.session.add(testimonial)
        db.session.commit()
        flash('Testimonial Updated Successfully!')
        return redirect(url_for('user.userprofile',firstname=firstname))
    form.title.data =  testimonial.title
    form.description.data = testimonial.description
    return render_template('testimonials/edit_testimonial.html',form=form,tid=tid)


@testimonials.route('/<tid>/delete_testimonial', methods=['GET','POST'])
@login_required
def delete_testimonial(firstname, tid):
    testimonial = Testimonials.query.filter_by(id=tid).first_or_404()
    db.session.delete(testimonial)
    db.session.commit()
    flash('Testimonial Deleted Successfully!')
    return redirect(url_for('user.userprofile',firstname=firstname))
