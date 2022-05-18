from app import app
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'roger'}
    return render_template('index.html', title='Home', user=user)

@app.route('/game')
def game():
	user = {'username': 'Roger'}
	return render_template('game.html', title='Play', user=user)
	
@app.route('/rule')
def rule():
	user = {'username': 'Roger'}
	return render_template('rule.html', title='rule', user=user)
	
@app.route('/post')
def index2():
    user = {'username': 'Roger'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'congradulations!!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'good job!'
        },
        {
		'author': {'username': 'rogerson'},
		'body' : 'could you follow me and play with me'
        }
    ]
    return render_template('post.html', title='Message', user=user, posts=posts)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
