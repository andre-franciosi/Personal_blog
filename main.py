from flask import Flask, render_template, request, session, redirect, url_for
import os

class User:
    def __init__(self, id, username, password):
        self.id =id
        self.username = username
        self.password = password
    
    def __repr__(self) :
        return f'<Users: {self.username}>'

users = []
users.append(User(1,username='Andre',password='123'))
users.append(User(2,username='Ricardo',password='321'))

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
    if request.method == 'POST':
        session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user.id'] = user.id
            return redirect(url_for('index'))
        return redirect(url_for('login'))

    return render_template('login.html')
#error pages

# Invalida URL (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error (500)
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500
