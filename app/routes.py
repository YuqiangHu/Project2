from app import app
from flask import render_template, flash, request, redirect,url_for
from app.forms import LoginForm
from flask_login import current_user, login_user
from app.models import User
from flask_login import logout_user
from flask_login import login_required
from app import db
from app.forms import RegistrationForm
from datetime import datetime
import json



@app.route('/')
@app.route('/index')
def index():
    
    return render_template('index.html', title='Home')


	
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
@login_required
def shudu():
    if request.method == "GET":
    	return render_template('shudu.html', title='shudu')
    else:	
    	data = request.get_json()
    	print(data["best_time"])
    	
    	current_user.besttime = int(data["best_time"])
    	
    	#p = User(besttime="current_user.besttime")
    	#db.session.add(p)
    	db.session.commit()

    	
    	print (current_user.besttime)
    	return "save successful"
    	
@app.route('/rank', methods=['GET', 'POST'])
def rank():
    result = []
    rank =User.query.order_by("besttime").all()
    for one_gamer in rank:
        temp_dict = dict()
        
        temp_dict["username"] = one_gamer.username
        temp_dict["besttime"] = one_gamer.besttime
        result.append(temp_dict)
    return render_template('rank.html', title='rank', rank_list=result)


@app.route('/admin1', methods=['GET', 'POST'])
@login_required
def admin1():
    result = []
    rank =User.query.order_by("id").all()
    for one_gamer in rank:
        temp_dict = dict()
        temp_dict["id"] = one_gamer.id
        temp_dict["username"] = one_gamer.username
        temp_dict["email"] = one_gamer.email
        temp_dict["besttime"] = one_gamer.besttime
       
        result.append(temp_dict)
             
    if current_user.access == 0:
    		return render_template('admin1.html', title='manage page', rank_list=result)
    else:
    		return render_template('index.html', title='Home')
		

 

@app.route('/mypage')
@login_required
def mypage():
    user = {'username': 'Roger'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Congradulations!!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Good Job!'
        },
        {
		'author': {'username': 'rogerson'},
		'body' : 'Could You Follow Me and Play With Me'
        }
    ]
    time =current_user.besttime
    return render_template('user.html', title='Message', user=user, posts=posts,time=time)
    

