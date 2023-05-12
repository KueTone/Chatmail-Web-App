from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm
import sys


myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
    
myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

if sys.platform != 'darwin':
# Windows pathing
    UPLOAD_FOLDER = 'app\static\images'
# Mac pathing
else:
    UPLOAD_FOLDER = 'app/static/images'

myapp_obj.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


flask_change_password = ChangePassword(min_password_length=1, rules=None)
flask_change_password.init_app(myapp_obj)


db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)
login.login_view = 'login'

migrate = Migrate(myapp_obj, db, render_as_batch=True)

from app import routes, models