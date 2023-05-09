from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_change_password import ChangePassword, ChangePasswordForm, SetPasswordForm

from flask_mail import Mail, Message

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
    
myapp_obj.config.from_object(Config)

flask_change_password = ChangePassword(min_password_length=1, rules=None)
flask_change_password.init_app(myapp_obj)


db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)
login.login_view = 'login'

migrate = Migrate(myapp_obj, db)

mail = Mail(myapp_obj)

myapp_obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
myapp_obj.config['MAIL_PORT'] = 465
myapp_obj.config['MAIL_USE_SSL'] = True
myapp_obj.config['MAIL_USE_TLS'] = False
myapp_obj.config['MAIL_USERNAME'] = 'someEmail@gmail.com'
myapp_obj.config['MAIL_PASSWORD'] = 'somePassword'

from app import routes, models
