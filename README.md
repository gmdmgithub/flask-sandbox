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
-- $User.query.all() # get the data
-- $post = Post(....) #the same
# to create modules 
1. move files to the folder ie app
2. create file __init_.py and move configuration
3. in app.py (any main file) leave "from folder import app"
4. create routs.py to move routs and models.py to move model data
