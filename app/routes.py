from app import app
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index1():
    user = {'username': 'm'}
    return '''
<html>
    <head>
        <title>Home Page - rogerblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''

@app.route('/template')
def index():
    user = {'username': 'roger'}
    return render_template('index.html', title='Home', user=user)

@app.route('/game')
def gme():
	return "this is my game"
@app.route('/post')
def index2():
    user = {'username': 'Roger'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
		'author': {'username': 'rogerson'},
		'body' : 'this is try'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index1'))
    return render_template('login.html', title='Sign In', form=form)
