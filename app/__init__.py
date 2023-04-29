from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_mail import Mail, Message
myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

myapp_obj.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)

login.login_view = 'login'

mail = Mail(myapp_obj)

myapp_obj.config['MAIL_SERVER'] = 'smtp.gmail.com'
myapp_obj.config['MAIL_PORT'] = 465
myapp_obj.config['MAIL_USE_SSL'] = True
myapp_obj.config['MAIL_USE_TLS'] = False
myapp_obj.config['MAIL_USERNAME'] = 'someEmail@gmail.com'
myapp_obj.config['MAIL_PASSWORD'] = 'somePassword'

from app import routes, models
