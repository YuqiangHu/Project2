from app import app
from flask import render_template, flash, request, redirect,url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from app import db
from app.forms import RegistrationForm
import json

from flask_admin.contrib.sqla import ModelView

@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')

@app.route('/game')
def game():
	user = {'username': 'Roger'}
	return render_template('game.html', title='Play', user=user)
	
@app.route('/rule')
def rule():
	user = {'username': 'Roger'}
	return render_template('rule.html', title='rule', user=user)
	
@app.route('/post')
@login_required
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

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()    
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/shudu', methods=['GET', 'POST'])
def shudu():
    if request.method == "GET":
    	return render_template('shudu.html', title='shudu')
    else:	
    	data = request.get_json()
    	print(data["best_time"])
    	# TODO
    	
    	return "save successful"
    

