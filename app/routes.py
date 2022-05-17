from app import app
from flask import render_template, flash, redirect,url_for
from app.forms import LoginForm



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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index1'))
    return render_template('login.html', title='Sign In', form=form)
