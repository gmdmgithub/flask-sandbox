from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
import secrets
from PIL import Image

from flask_sandbox import app, bcrypt, db, mail
from flask_sandbox.models import User, Post
from flask_sandbox.config import about_p, account_p, home_p, login_p, posts, register_p, new_post_p, post_p, pagin_per_page, rest_request_p, rest_password_p
from flask_sandbox.users.utils import save_image, send_email
from flask_sandbox.users.forms import RegistrationForm, LoginForm, UpdateAccountForm, ResetRequestForm, RestetPassword

from flask_login import login_user, current_user, logout_user, login_required


users = Blueprint('users',__name__)


@users.route("/user_posts/<int:usr_id>",methods=['GET'])
def user_posts(usr_id):
    page = request.args.get('page',1,type=int)
    #usr_id = request.args.get('usr_id',type=int)
    user = User.query.filter_by(id=usr_id).first_or_404()
    posts = Post.query.filter_by(user_id=usr_id)\
                    .order_by(Post.date.desc())\
                    .paginate(per_page=pagin_per_page, page=page)
    # TODO - change home.html to dedicated
    return render_template('home.html',param=home_p, postList=posts,page=page,usr_id=usr_id) #"<h1>Hi there - here is flask - no restart</h1>"

#route for registration form
@users.route('/register',methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, password=hashed_pass,email=form.email.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! Please login to the system', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', param=register_p, form=form)

#route login form
@users.route('/login',methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        db_user = User.query.filter_by(username=form.username.data).first()
        if db_user and bcrypt.check_password_hash(db_user.password,form.password.data):
            login_user(db_user,form.rememberMe.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login unsuccessful', 'unsuccess')  
    return render_template('login.html', param=login_p, form=form)

#route logout form
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

#rout for account user page
@users.route('/account',methods=['GET', 'POST'])
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
        flash(f'Your account has been sucessfully update', 'success')  
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
        
    return render_template('account.html', param=account_p, image_file=image_file, form=form)


@users.route('/rest_request',methods=['GET','POST'])
def rest_request():
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    form = ResetRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()
        # TODO senading email
        send_email(user)
        flash(f'Your request has been processed', 'success')
        return redirect(url_for('main.home'))
    return render_template('reset_request.html',param=rest_request_p, form=form)


@users.route('/reset_password/<token>',methods=['GET','POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('users.account'))
    user = User.veryfy_auth_token(token)
    if user is None:
        flash(f'Invalied token', 'unsuccess')
        return redirect(url_for('main.home'))
    form = RestetPassword()
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user.password = hashed_pass
        db.session.commit()
        flash(f'Your password has been succesfuly changed', 'success')
        return redirect(url_for('main.home'))
    return render_template('reset_password.html',param=rest_password_p, form=form)
