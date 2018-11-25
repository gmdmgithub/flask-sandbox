# flask-sandbox
Fisrt flask sandbox project
# instal flask
pip install Flask
# for env
pip install python-dotenv
# for secret you can use
$python
-- $import secrets
-- $secrets.token_hex(16)
# for database install
$pip install flask-sqlalchemy
from flask_sqlalchemy import SQLAlchemy
# to create db
$python
-- $from app import db
-- $db.create_all()
-- $from app import User, Post
-- $usr = User(username='test',password='password',email='test@test.com')
-- $db.session.add(usr) #add couple more 
-- $db.session.commit()
