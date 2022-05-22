from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager





app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'






from app import routes, models 

#@app.before_request 
#def insert(): 
#	from app import db
#	from app.models import User
#	us1 = User(username='admin',email='5505@uwa.edu.au',password_hash='123456',access=0)
#	us2 = User(username='yuqiang',email='23081533@uwa.edu.au',password_hash='123456',access=0)
#	db.session.add_all([us1,us2])
#	db.session.commit()
