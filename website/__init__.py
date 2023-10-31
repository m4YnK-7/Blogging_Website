from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY']='t3am.t4r|k3y'

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    return app