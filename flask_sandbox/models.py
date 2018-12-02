from datetime import datetime
from flask_sandbox import db, login_manager, ma
from flask import current_app
from flask_login import UserMixin #imports neccessary fields for the user

from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)



#function to keep the user session https://flask-login.readthedocs.io/en/latest/
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# lets create model classes
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    posts = db.relationship('Post',backref='author',lazy=True)
    
    def generate_auth_token(self, expiration = 600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps({ 'usr_id': self.id }).decode('utf-8') #tokem may have as many information as you need
    
    # method is static does not require object
    @staticmethod
    def veryfy_auth_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        user = User.query.get(data['usr_id'])
        return user

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.date}')"

