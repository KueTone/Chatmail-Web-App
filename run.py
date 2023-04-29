from app import myapp_obj
# import os
# from flask import Flask, render_template, request, url_for, flash, redirect
# from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy.sql import func

# # absolute pathname of run.py
# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] =\
#     'sqlite:///' + os.path.join(basedir, 'sql/email.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)


# def get_db_connection():
#     conn = sqlite3.connect('sql/email.db')
#     conn.row_factory = sqlite3.Row
#     return conn


# if __name__ == "__main__"
myapp_obj.run(debug=True)
