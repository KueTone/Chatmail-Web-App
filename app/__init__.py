from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm


myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
    
myapp_obj.config.from_object(Config)

UPLOAD_FOLDER = 'static/images/'
flask_change_password = ChangePassword(min_password_length=1, rules=None)
flask_change_password.init_app(myapp_obj)


db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)
login.login_view = 'login'

migrate = Migrate(myapp_obj, db, render_as_batch=True)

from app import routes, models