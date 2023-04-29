from flask import render_template
from flask import redirect
from flask import flash
from .forms import LoginForm
from app import myapp_obj
from app import db
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from .models import User


@myapp_obj.route('/')
def index():
    # conn = get_db_connection()
    # posts = conn.execute('SELECT * FROM posts').fetchall()
    # conn.close()
    return render_template('index.html')


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


@myapp_obj.route("/welcome", methods=['GET', 'POST'])
def login():
    # create form
    form = LoginForm()
    # if form inputs are valid
    if form.validate_on_submit():
        # search database for username
        # user = User.query.filter_by(...)
        # check the password
        # if password matches
        # login_user(user)
        flash(
            f'Here are the input {form.username.data} and {form.password.data}')
        return redirect('/')
    return render_template('login.html', form=form)


@myapp_obj.route("/members/<string:name>/")
def getMember(name):
    return escape(name)
