from flask import Flask, render_template

app = Flask(__name__)

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

#error pages

# Invalida URL (404)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Internal Server Error (500)
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500