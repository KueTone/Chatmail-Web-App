from flask import render_template
from flask import redirect
from flask import flash
from flask import url_for
from flask import request
from .forms import LoginForm
from app import myapp_obj
from app import db
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User, Post
from werkzeug.urls import url_parse

@myapp_obj.route('/')
@myapp_obj.route('/index')
@login_required
def index():
    # users = User.query.all()
    posts = Post.query.all()
    return render_template('index.html', posts=posts)

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


@myapp_obj.route('/profile')
def profile():
    engine = db.create_engine('sqlite:///census.sqlite')
    connection = engine.connect()
    metadata = db.MetaData()
    census = db.Table('census', metadata, autoload=True, autoload_with=engine)

    query = db.select([census])

    return render_template('profile.html', username=form.query, password=form.password, email='@sjsu.edu')


@myapp_obj.route('/editProfile', methods=['GET', 'POST'])
def editProfile():
    return render_template('editProfile.html')

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
    return redirect(url_for('index'))

@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
