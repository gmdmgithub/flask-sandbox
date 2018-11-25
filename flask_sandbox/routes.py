from flask import render_template, url_for, flash, redirect, request
from flask_sandbox import app, bcrypt, db
from flask_sandbox.models import User, Post
from flask_sandbox.reg_form import RegistrationForm
from flask_sandbox.login_form import LoginForm

from flask_login import login_user, current_user, logout_user, login_required

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
account_p = {
    'active':'account',
    'menu': True,
    'title': 'Account page'
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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pass,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Please login to the system', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', param=register_p, form=form)

#route login form
@app.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        db_user = User.query.filter_by(username=form.username.data).first()
        if db_user and bcrypt.check_password_hash(db_user.password,form.password.data):
            login_user(db_user,form.rememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login unsuccessful', 'unseccessful')  
    return render_template('login.html', param=login_p, form=form)

#route logout form
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))  

#rout for account user page
@app.route('/account')
@login_required
def account():
    return render_template('account.html', param=account_p)



#not foud - bed address - at the and of routs
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('not-found.html')
    