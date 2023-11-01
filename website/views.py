from flask import Blueprint, render_template, url_for, request, flash,redirect
from .models import User
from flask_login import login_user, login_required, logout_user, current_user
# from werkzeug.security import generate_password_hash,check_password_hash
from . import db
views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def reg():
	if request.method == 'POST':
		email = request.form.get('email')
		first_name = request.form.get('first_name')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
			
		user = User.query.filter_by(email=email).first()
		if user:
			flash('Email already exists.', category='error')
			print("exists")
		elif password1 != password2:
			flash('Passwords don\'t match.', category='error')
			print("Wrong pass")
		else:
			new_user = User(email=email, name=first_name, password=password1)
			db.session.add(new_user)
			db.session.commit()
			login_user(user ,remember=True)
			flash('Account created successfully', category='success')
			print("Account created")
			return redirect(url_for('views.home'))

	return render_template('register.html',user=current_user)


@views.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('views.login'))

@views.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		email = request.form.get('email')
		password = request.form.get('password')		
		print(email)
		user = User.query.filter_by(email=email).first()
		if user:
			print("Account created")
			if user.password == password:
				flash('Logged in successfully!', category='success')
				login_user(user, remember=True)
				print("Logged in successfully")
				return redirect(url_for('views.home'))	
				
			else:
				flash('Incorrect password, try again.', category='error')
				print("Wrong pass")
		else:
			flash('Email does not exist.', category='error')
			print("NO email")

	return render_template("login.html",user=current_user)


@views.route('/home')
def home():
	return render_template('home.html',user=current_user)

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