from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from hashlib import md5
from flask_login import UserMixin


# User Table that is generated for each user made when registering
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    # profile
    name = db.Column(db.String(32), nullable=True)
    age = db.Column(db.Integer, nullable=True)
    bio = db.Column(db.Text, nullable=True)
    profilePic = db.Column(db.String(),  nullable=True)
    followers = db.Column(db.Integer, nullable=True)
    following = db.Column(db.Integer, nullable=True)
    repositories = db.Column(db.Integer, nullable=True)

    repositories_name = db.Column(db.String(), nullable=True)

    recipient = db.relationship('Post', backref='receiver', lazy='dynamic', foreign_keys='Post.receive_id')
    author = db.relationship('Post', backref='author', lazy='dynamic', foreign_keys='Post.author_id')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
        
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def __repr__(self):
        return f'<user {self.username}: {self.name}>'

# Post Table used to store posts with both an author back reference and receiver back reference
# Auther and Recipient back reference allows for ease of use when filtering
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    
    receive_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'
    
# Blocklist contains list of blocked Users that won't be displayed in the main index.html file
class BlockList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32))
    def __repr__(self):
        return f'<Post {self.username}>'

# Task contains all tasks that were made in checklist. Contains timestamp that it was made in.
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime(), default=datetime.now)
    text = db.Column(db.String(), nullable=False)
    complete = db.Column(db.Boolean)
    
    def __repr__(self):
        return f'<Task {self.id}: {self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

