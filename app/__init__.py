from flask import Flask
from .config import Config
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_migrate import Migrate

myapp_obj = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
    
myapp_obj.config.from_object(Config)

db = SQLAlchemy(myapp_obj)

login = LoginManager(myapp_obj)
login.login_view = 'login'

migrate = Migrate(myapp_obj, db)

from app import routes, models
