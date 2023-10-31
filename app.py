from flask import Flask, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from markupsafe import escape
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(200), nullable=False)
	completed = db.Column(db.Integer, default=0)
	date_created = db.Column(db.DateTime, default=datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/')
def home():
	return render_template('index.html')

app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'




if __name__ == '__main__':
	app.run()
