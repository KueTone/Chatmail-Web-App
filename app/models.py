from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from hashlib import md5
from flask_login import UserMixin
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    # profile
    first = db.Column(db.String(32), nullable=True)
    last = db.Column(db.String(32), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profilePic = db.Column(db.String(),  nullable=True)

    recipient = db.relationship('Post', backref='receiver', lazy='dynamic', foreign_keys='Post.author_id')
    author = db.relationship('Post', backref='author', lazy='dynamic', foreign_keys='Post.receive_id')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
        
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def __repr__(self):
        return f'<user {self.username}: {self.first}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    receive_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

