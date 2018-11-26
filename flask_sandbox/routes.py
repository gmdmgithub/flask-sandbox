from flask import render_template, url_for, flash, redirect, request
import secrets
import os
from PIL import Image
from flask_sandbox import app, bcrypt, db
from flask_sandbox.models import User, Post
from flask_sandbox.forms.registration import RegistrationForm
from flask_sandbox.forms.login import LoginForm
from flask_sandbox.forms.account import UpdateAccountForm

from flask_login import login_user, current_user, logout_user, login_required

from flask_sandbox.config import about_p, account_p, home_p, login_p, posts, register_p


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

def save_image(image):
    random_hex = secrets.token_hex(8)
    _f_name, f_ext = os.path.splitext(image.filename) #when you do not use variable  start it _ 
    image_filename = random_hex+f_ext
    image_path = os.path.join(app.root_path,'static/profile_img',image_filename)
    
    output_size = (250, 250)
    i = Image.open(image)
    i.thumbnail(output_size)
    i.save(image_path)
    
    return image_filename

#rout for account user page
@app.route('/account',methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    image_file = url_for('static',filename='profile_img/'+current_user.image_file)
    if form.validate_on_submit():
        if form.image.data:
            f_image = save_image(form.image.data)
            current_user.image_file = f_image
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash(f'Your account has been sucessfully update', 'seccessful')  
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
        
    return render_template('account.html', param=account_p, image_file=image_file, form=form)



#not foud - bed address - at the and of routs
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('not-found.html')
    