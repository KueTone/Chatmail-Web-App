import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/welcome', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # future change will incorporate a simple textfile database and maybe a SQL database if provded time
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/editProfile')
def editProfile():
    return render_template('editProfile.html')


if __name__ == "__main__":
    app.run(debug=True)
