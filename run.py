from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


# @app.route('/')
# def welcome():
#     return render_template('welcome.html')
# # Route for handling the login page logic


# Route for handling the login page logic
@app.route('/welcome', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # future change will incorporate a simple textfile database and maybe a SQL database if provded time
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/editProfile')
def editProfile():
    return render_template('editProfile.html')

@app.route('/create', methods=['GET', 'POST'])
def createAcct():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin':
            error = 'Username already in use. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('acctCreate.html', error = error)



if __name__ == "__main__":
    app.run(debug=True)
