from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sandbox.config_app import Config

from flask_mail import Mail

from flask_marshmallow import Marshmallow

import logging

# logger = logging.getLogger(__name__) ##- if you what to have seperate logging files and evoid problem with import

# logger.setLevel(logging.DEBUG)

# formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(filename)s:'+\
#                     '%(module)s:%(lineno)d:%(message)s:'+\
#                     '%(processName)s:%(process)d:%(threadName)s:%(thread)d')


# file_hendler = logging.FileHandler('logfile.log')
# file_hendler.setFormatter(formatter)
# file_hendler.setLevel(logging.DEBUG)

# stream_hendler = logging.StreamHandler() ##we can specify as meny hendler as we want
# stream_hendler.setFormatter(formatter)
# stream_hendler.setLevel(logging.INFO)

# logger.addHandler(file_hendler)
# logger.addHandler(stream_hendler)


logging.basicConfig(level=logging.DEBUG,filename='logfile.log',
                    format='%(asctime)s:%(levelname)s:%(filename)s:'+\
                    '%(module)s:%(lineno)d:%(message)s:'+\
                    '%(processName)s:%(process)d:%(threadName)s:%(thread)d')

# lets create db connection
db = SQLAlchemy()

# let create mail
mail = Mail()

##use bcrypt to hash
bcrypt = Bcrypt()

# use marshmallow
ma = Marshmallow()

#login manager
login_manager = LoginManager()
#login rout (function) when login_required not meet
login_manager.login_view = 'users.login'

#import routs here to do not have circulate init
#from flask_sandbox import routes - it was before bluprint introduction



def create_app(config_class=Config):
    
    #set configuration to the app
    app = Flask(__name__)
    
    #simpler way - create Config class
    app.config.from_object(Config)
    logging.debug('config file has been read')
    
    #init all utils db, mail, crypt, user ...
    db.init_app(app)
    mail.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    ma.init_app(app)
    
    #add all routs
    from flask_sandbox.users.routs import users
    from flask_sandbox.posts.routs import posts
    from flask_sandbox.main.routs import main
    from flask_sandbox.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app


