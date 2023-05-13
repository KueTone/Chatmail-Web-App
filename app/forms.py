from flask_wtf import FlaskForm
from flask_wtf.file import FileField
from datetime import datetime
from wtforms.fields import DateField, TimeField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, IntegerField, DateTimeField
from wtforms.validators import DataRequired, Length

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
    
class ComposeEmailForm(FlaskForm):
    recipient = StringField('Username', validators=[DataRequired()])
    body = StringField('Body', validators=[DataRequired(), Length(min=0, max=140)])
    send = SubmitField('Send') 

class EditProfileForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')
    email = StringField('Email')
    name = StringField('name')
    last = StringField('Last')
    bio = TextAreaField('About me')
    age = IntegerField('Age')
    submit = SubmitField('Save Changes')
    profilePic = FileField("Profile Pic")
    github = StringField("Github Username")
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Register')

    
class BlockListForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    submit = SubmitField('BlockList')


class ChecklistForm(FlaskForm):
    text = StringField('Text', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', default=datetime.now().strftime("%Y-%m-%d"))
    time = TimeField('Time', format='%H:%M', default=datetime.now().strftime("%H:%M"))
    submit = SubmitField('Add Task')

