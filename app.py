from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from reg_form import RegistrationForm
from login_form import LoginForm
from os.path import join, dirname
import os
from dotenv import load_dotenv
from datetime import datetime

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
#db.init_app(app)

# lets create model classes
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    posts = db.relationship('Post',backref='Author',lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), nullable=False)
    date = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.id}', '{self.title}', '{self.date}')"


#lets add some posted data (simply not from db)
posts = [
    {
        'author': 'John Doe',
        'title': 'My best friend',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-01-15'
    },
    {
        'author': 'Janet Jackson',
        'title': 'My brother',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-02-15'
    },
    {
        'author': 'John Kennedy',
        'title': 'My country',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-03-15'
    }
]

home_p ={
    'active':'home',
    'menu': True,
    'title' : 'Home page'
}
about_p ={
    'active':'about',
    'menu': True,
    'title' : 'About page'
}

register_p = {
    'active':'registration',
    'menu': False,
    'title': 'Registration page'
}

login_p = {
    'active':'login',
    'menu': False,
    'title': 'Login page'
}

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',param=home_p, postList=posts) #"<h1>Hi there - here is flask - no restart</h1>"

#anbout page
@app.route("/about")
def about():
    return render_template('about.html', param=about_p, title="About page")

#route for registration form
@app.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', param=register_p, form=form)

#route login form
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'test@test.com' and form.password.data == '123456':
            flash(f'Login to the system {form.username.data}!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Incorect username or/and password','unseccessful')
    return render_template('login.html', param=login_p, form=form)

#not foud - bed address
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('not-found.html')
    

if __name__ == "__main__":
    app.run(debug=True)
