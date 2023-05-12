from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask import request
from .forms import LoginForm, EditProfileForm
from app import myapp_obj
from app import db
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User, Post
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
import uuid as uuid
import os

@myapp_obj.route('/')
@myapp_obj.route('/index')
def index():
    users = User.query.all()
    posts = Post.query.all()
    return render_template('index.html', users=users, posts=posts)

# @myapp_obj.route('/welcome', methods=['GET', 'POST'])
# def login():
#     error = None
#     if request.method == 'POST':
#         # future change will incorporate a simple textfile database and maybe a SQL database if provded time
#         if request.form['username'] != 'admin' or request.form['password'] != 'admin':
#             error = 'Invalid Credentials. Please try again.'
#         else:
#             return redirect(url_for('index'))
#     return render_template('login.html', error=error)


@myapp_obj.route('/profile/<username>/')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()

    return render_template('profile.html', user = user)


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
        elif section == 'first':
            current_user.first      = form.first.data
        elif section == 'last':
            current_user.last       = form.last.data
        elif section == 'bio':
            current_user.bio        = form.bio.data
        elif section =='profilePic':
            current_user.profilePic = request.files['profilePic']
            picFilename = secure_filename(current_user.profilePic.filename)
            picName = str(uuid.uuid1()) +"_"+ picFilename
            saver = request.files['profilePic']
            
            current_user.profilePic = picName
            saver.save(os.path.join(myapp_obj.config['UPLOAD_FOLDER'], picName))

            

        db.session.commit()
        
        flash('Your changes have been saved.')
        return redirect(url_for('profile', username = current_user.username))
    elif request.method == 'GET':
        form.username.data          = current_user.username
        form.email.data             = current_user.email
        form.first.data             = current_user.first
        form.last.data              = current_user.last
        form.bio.data               = current_user.bio
    return render_template('editProfile.html', title='Edit Profile', form=form, section=section)

# @app.route('/welcome', methods=['GET', 'POST'])
@myapp_obj.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user: {}, password: {}, remember_me={}'.format(form.username.data, form.password.data, form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()
        # pass = User.query.filter_by(password=form.password.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password: {}'.format(user))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@myapp_obj.route('/logout')
def logout():
    logout_user()
    flash('You are being logged out...')
    return redirect(url_for('index'))

@myapp_obj.route('/delete/<id>/')
def delete_user(id):
    
    return redirect(url_for('index'))
    

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
@myapp_obj.route("/compose_email", methods=['GET', 'POST'])
def compose_email():
        return render_template('sendEmail.html')
