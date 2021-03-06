from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from werkzeug.debug import DebuggedApplication
from config import Config
import os
# from os import environ

from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

# from flask.ext.bcrypt import Bcrypt

# environ.get('DATABASE_URL')
def create_app():
    app = Flask(__name__)
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:flask@localhost:5432/user_events'
    app.config.from_object(Config)
    app.secret_key = os.urandom(32)
    app.debug = True
    csrf = CSRFProtect(app)
    csrf.init_app(app)
    print( 'SQLALCHEMY_DATABASE_URI', app.config['SQLALCHEMY_DATABASE_URI'])
    if app.debug:
        app.wsgi_app = DebuggedApplication(app.wsgi_app, evalex=True)

    return app

app = create_app()
db = SQLAlchemy(app)
# db.create_all()
migrate = Migrate(app, db)

login_manager = LoginManager()
login_manager.login_view = 'login'
# # login_manager.session_protection = "strong"
login_manager.init_app(app)

bcrypt = Bcrypt(app)

from app import routes, models, forms
db.create_all()
