from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask import request
from sqlalchemy import or_
from sqlalchemy import desc
from .forms import LoginForm, EditProfileForm, RegistrationForm, ComposeEmailForm, ChecklistForm, BlockListForm
from app import myapp_obj
from app import db
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User, Post, Task, BlockList
# unique user id for profile image
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
import uuid as uuid
#saving image
import os
#github api
import requests
import json
from github import Github
from datetime import datetime

# Functions as the welcome page and the home page of the user
@myapp_obj.route('/', methods=['GET', 'POST'])
@myapp_obj.route('/index', methods=['GET', 'POST'])
def index():
    # Takes in information from the tables shown below
    users = User.query.all()

    search = request.args.get('q')
    if (search==None):
        search = ""
    search1 = "%{}%".format(search)
    posts = Post.query.filter(Post.body.like(search1)).order_by(desc(Post.id)).all()
    

    blocks = BlockList.query.all()
    
    form = ComposeEmailForm()
    
    # Once the user pressses send, the database table Post should update
    # Once updated, will redirect back to index and display the new posts.
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.recipient.data).first()
        if user is None:
            flash('Invalid username: {}'.format(form.recipient.data))
            return redirect(url_for('index'))
        post = Post(body = form.body.data, author_id = current_user.id, receive_id = user.id)
        db.session.add(post)
        db.session.commit()
        flash('Sending post...')
        return redirect(url_for('index'))
    return render_template('index.html', users=users, posts=posts, title='Compose', form=form, blocks=blocks)

@myapp_obj.route('/index/<user>/', methods=['GET', 'POST'])
@login_required
def indexU(user):
    users = User.query.all()
    receiveid = User.query.filter(User.username == user).first().id
    search = request.args.get('q')
    if (search==None):
        search = ""
    search1 = "%{}%".format(search)
    posts = Post.query.filter(Post.body.like(search1),or_(Post.author_id==current_user.id,Post.author_id==receiveid),or_(Post.receive_id==receiveid,Post.receive_id==current_user.id)).order_by(desc(Post.id)).all()
    
    form = ComposeEmailForm()
    form.recipient.data = 'user'
    if form.validate_on_submit():
        post = Post(body = form.body.data, author_id = current_user.id, receive_id = receiveid)
        db.session.add(post)
        db.session.commit()
        flash('Sending post...')
        return redirect(url_for('indexU', user=user))
    return render_template('index.html', users=users, posts=posts, form=form)
  
@myapp_obj.route('/profile/<username>/')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('profile.html', user = user)

# Allows user to edit certain parts of the profile page such as photo, username, password
@myapp_obj.route('/editProfile/<section>/', methods=['GET', 'POST'])
@login_required
def edit_profile(section):
    form = EditProfileForm()

    if request.method == 'POST':
        if section == 'username':
            current_user.username   = form.username.data
        elif section == 'password':
            current_user.set_password(form.password.data)
        elif section == 'email':
            current_user.email      = form.email.data
        elif section == 'name':
            current_user.name      = form.name.data
        elif section == 'bio':
            current_user.bio        = form.bio.data
        elif section =='profilePic':
            current_user.profilePic = request.files['profilePic']
            picFilename = secure_filename(current_user.profilePic.filename)
            picName = str(uuid.uuid1()) +"_"+ picFilename
            saver = request.files['profilePic']
            
            current_user.profilePic = picName
            saver.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], picName))
        elif section =='github':
            if current_user.username != form.github.data:
                flash("Not matching usernames. Please try again...")
                return redirect(url_for('edit_profile', title='Edit Profile', form=form, section = 'github'))
            return redirect(url_for('connectGithub', username = form.github.data))
            
        db.session.commit()
        
        flash('Your changes have been saved.')
        return redirect(url_for('profile', username = current_user.username))
    elif request.method == 'GET':
        form.username.data          = current_user.username
        form.email.data             = current_user.email
        form.name.data              = current_user.name
        form.bio.data               = current_user.bio
        form.github.data            = current_user.username
    return render_template('editProfile.html', title='Edit Profile', form=form, section=section)

# Login Page
@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password: {}'.format(user))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

# Register User
@myapp_obj.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        user.name = form.name.data

        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)

# Logout which redirects the user from anywhere back to index and logs out using logout_user()
@myapp_obj.route('/logout')
def logout():
    logout_user()
    flash('Sorry to see you go! Logging out...')
    return redirect(url_for('index'))

# Deletes the user
@myapp_obj.route('/delete/', methods=['GET', 'POST'])
@login_required
def delete_user():
    userDelete = User.query.get_or_404(current_user.id)
    postDelete = Post.query.filter(Post.receive_id == current_user.id).delete()
    postDelete2 = Post.query.filter(Post.author_id == current_user.id).delete()
    db.session.delete(userDelete)
    db.session.commit()
    flash("Sorry to see you go! Deleting User & all Posts by and to User...")
    return redirect(url_for('index'))

# Deletes post
@myapp_obj.route('/deletePost/<id>/', methods=['GET', 'POST'])
@login_required
def deletePost(id):
    postDelete = Post.query.get(id)
    db.session.delete(postDelete)
    db.session.commit()
    flash("Deleting Post")
    return redirect(url_for('index'))    

# Connects to Github API
# Automatically stores new Github data into profile

@myapp_obj.route("/github/<string:username>/")
@login_required
def connectGithub(username):
    
    # Github authentication
    token = "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"

    # gh_session = requests.Session()
    # gh_session.auth = (username , token)
    user = Github().get_user(username)

    url = f"https://api.github.com/users/{username}"


    repos = ''
    
    for repo in user.get_repos():
        repos += "#" + repo.full_name

        # flash(repos)

    current_user.name           = user.name
    current_user.bio            = user.bio
    current_user.followers      = user.followers
    current_user.following      = user.following
    current_user.repositories   = user.public_repos
    current_user.repositories_name   = repos
    db.session.commit()
    
    return redirect(url_for('profile', username = username))
    
@myapp_obj.route('/block', methods=['GET', 'POST'])
@login_required
def block():
    form = BlockListForm()
    if form.validate_on_submit():
        blocked = BlockList(username = form.username.data)
        db.session.add(blocked)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('blocklist.html', title='BlockList', form=form)

@myapp_obj.route('/compose_email', methods=['GET', 'POST'])
@login_required
def compose_email():
    form = ComposeEmailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.recipient.data).first()
        if user is None:
            flash('Invalid username: {}'.format(form.recipient.data))
            return redirect(url_for('compose_email'))
        # user = User.query.filter_by(username = form.recipient.data).first_or_404()

    #   post = Post(author=current_user, recipient=recipient, subject=form.subject.data, body=form.body.data)
        post = Post(body = form.body.data, author_id = current_user.id, receive_id = user.id)
        db.session.add(post)
        db.session.commit()
        flash('Sending post...')
        return redirect(url_for('index'))
    return render_template('sendingEmail.html', title='Compose', form=form)

@myapp_obj.route('/editPost/<id>/', methods=['GET', 'POST'])
@login_required
def editPost(id):
    form = ComposeEmailForm()
    postEdit = Post.query.get(id)
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.recipient.data).first()
        if user is None:
            flash('Invalid username: {}'.format(form.recipient.data))
            return redirect(url_for('compose_email'))
        postEdit.receive_id = user.id
        postEdit.body = form.body.data
        db.session.add(postEdit)
    
        db.session.commit()
        flash("Post Edited")
        return redirect(url_for('index')) 
    elif request.method == 'GET':
        form.recipient.data = postEdit.receiver.username
        form.body.data = postEdit.body
    return render_template('sendingEmail.html', title='Compose', form=form)

    
@myapp_obj.route('/checklist', methods=['GET', 'POST'])
@login_required
def checklist():
    incomplete = Task.query.filter_by(complete=False).all()
    complete = Task.query.filter_by(complete=True).all()

    return render_template('checklist.html', incomplete=incomplete, complete=complete)

@myapp_obj.route('/newItem', methods=['GET', 'POST'])
@login_required
def createTask():
    form = ChecklistForm()
    if form.validate_on_submit():
        
        task = Task(text = form.text.data, complete = False)

        db.session.add(task)
        db.session.commit()
        flash("Task Added")
        return redirect(url_for('checklist'))
    
    return render_template('newItem.html', form = form)

@myapp_obj.route('/complete/<id>')
def complete(id):

    todo = Task.query.filter_by(id=int(id)).first()
    todo.complete = True
    db.session.commit()
    
    return redirect(url_for('checklist'))

@myapp_obj.route('/incomplete/<id>')
def incomplete(id):

    todo = Task.query.filter_by(id=int(id)).first()
    todo.complete = False
    db.session.commit()
    
    return redirect(url_for('checklist'))

@myapp_obj.route('/deleteTask/<id>')
def deleteTask(id):

    todo = Task.query.filter_by(id=int(id)).first()
    db.session.delete(todo)
    db.session.commit()
    
    return redirect(url_for('checklist'))
