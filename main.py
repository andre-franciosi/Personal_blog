from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect, CSRFError
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

csrf = CSRFProtect(app)

#Create Form class

class NameForm(FlaskForm):
    name = StringField("User", validators = [DataRequired()]) #Stringfield is the textbox  #With DataRequired the user have to put something in the field
    password = PasswordField("Password ", validators = [DataRequired()])
    submit = SubmitField("Log in") #Button

#Creating the first route

@app.route('/')

def index():
    num = [1,2,3,4,5]
    return render_template('index.html',
    num=num)

#User route (localhost:5000/user/name)

@app.route('/user/<name>')

def user(name):
    return render_template('user.html', user_name = name)

#Register page route

@app.route('/register', methods = ['GET', 'POST'])

def register():
    name = None
    password = None
    form = NameForm()
    #Validate form
    if form.validate_on_submit():
        name = form.name.data
        password = form.password.data
        form.name.data = ''
    return render_template('user_register.html',
    name = name,
    password = password,
    form = form)

#error pages

# Invalida URL (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error (500)
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500