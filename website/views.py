from flask import Blueprint, render_template, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def reg():
	if request.method == 'POST':
		email = request.form.get('email')
		first_name = request.form.get('firstName')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		
		user = User.query.filter_by(email=email).first()
		if user:
			flash('Email already exists.', category='error')
		elif password1 != password2:
			flash('Passwords don\'t match.', category='error')
		else:
			new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
			db.session.add(new_user)
			db.session.commit()
			login_user(new_user, remember=True)
			flash('Account created successfully', category='success')
			return redirect(url_for('views.home'))

	return render_template('register.html')

@views.route('/home')
def home():
	return render_template('home.html')

@views.route('/reading-list')
def readlst():
	return render_template('readlst.html')

@views.route('/notifications')
def noti():
	return render_template('noti.html')

@views.route('/subscriptions')
def subs():
	return render_template('subs.html')

@views.route('/wallet')
def wallet():
	return render_template('wallet.html')

@views.route('/profile')
def usr_prof():
	return render_template('profile.html')

@views.route('/settings')
def settings():
	return render_template('settings.html')