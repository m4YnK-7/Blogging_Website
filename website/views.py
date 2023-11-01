from flask import Blueprint, render_template, url_for

views = Blueprint('views', __name__)

@views.route('/')
def reg():
	return render_template('register.html')

@views.route('/home')
def home():
	return render_template('index.html')