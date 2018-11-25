from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join, dirname
import os
from dotenv import load_dotenv


# get configuration
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")


#set configuration to the app
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
# lets create db connection
db = SQLAlchemy(app)

#import routs here to do not have circulate init
from flask_sandbox import routes

