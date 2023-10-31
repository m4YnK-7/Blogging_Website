from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
def home():
	return render_template('index.html')

app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

# main driver function
if __name__ == '__main__':

	app.run()
