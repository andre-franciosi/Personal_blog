from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os

class UserForm(FlaskForm):
    user = StringField("What's your user?", validators = [DataRequired()])
    login = SubmitField("Log in")


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Creating the first route

@app.route('/')
def index():
    num = [1,2,3,4,5]
    return render_template('index.html',
    num=num)

#Register page route

@app.route('/login', methods = ['GET', 'POST'])
def login():
    user = None
    form = UserForm()
    if form.validate_on_submit():
        user = form.user.data
        form.user.data = ''
    return render_template('login.html',
    user = user,
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
