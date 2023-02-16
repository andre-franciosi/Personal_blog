from flask import Flask, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

class UserForm(FlaskForm):
    user = StringField("What's your user?", validators = [DataRequired()])
    email = StringField("What's your email?", validators = [DataRequired()])
    signup = SubmitField("Sign up")


app = Flask(__name__)
#Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#Secret Key
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(120), nullable = False, unique = True)
    date_added = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Name: %r>' % self.name

#Creating the first route

@app.route('/')
def index():
    num = [1,2,3,4,5]
    return render_template('index.html',
    num=num)

#Register page route

@app.route('/register', methods = ['GET', 'POST'])
def signup():
    user = None
    email = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(user=form.user.data, email = form.email.data)
            db.session.add(user)
            db.session.commit()
        user = user.form.data
        form.user.data = ''
        form.email.data = ''
    users = Users.query.order_by(Users.date_added)
    return render_template('signup.html',
    user = user,
    email = email,
    users = users,
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
