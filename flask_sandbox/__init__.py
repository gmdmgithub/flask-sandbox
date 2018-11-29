from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from os.path import join, dirname
import os
from dotenv import load_dotenv
from flask_mail import Mail

# get configuration
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
MAIL_SERVER = os.environ.get("MAIL_SERVER")
MAIL_PORT = os.environ.get("MAIL_PORT")
MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS")
MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

#set configuration to the app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# lets create db connection
db = SQLAlchemy(app)

#email config
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
# let create mail
mail = Mail(app)

##use bcrypt to hash
bcrypt = Bcrypt()

#login manager
login_manager = LoginManager(app)
#login rout (function) when login_required not meet
login_manager.login_view = 'users.login'

#import routs here to do not have circulate init
#from flask_sandbox import routes - it was before bluprint introduction
from flask_sandbox.users.routs import users
from flask_sandbox.posts.routs import posts
from flask_sandbox.main.routs import main

app.register_blueprint(users)
app.register_blueprint(posts)
app.register_blueprint(main)

