from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, current_app
from flask_sandbox.models import Post

from flask_sandbox.config import about_p, account_p, home_p, login_p, posts, register_p, new_post_p, post_p, pagin_per_page, rest_request_p, rest_password_p

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page',1,type=int)
    posts = Post.query.order_by(Post.date.desc()).paginate(per_page=pagin_per_page, page=page)
    # when paginate problem with sql update
    # for post in posts.items: 
    #     if not 'static' in post.author.image_file:
    #         post.author.image_file = "static/profile_img/"+post.author.image_file
    return render_template('home.html',param=home_p, postList=posts,page=page) #"<h1>Hi there - here is flask - no restart</h1>"


#anbout page
@main.route("/about")
def about():
    return render_template('about.html', param=about_p, title="About page")



################# END - GRAP ALL REQUESTS ################### 
#not foud - bed address - at the and of routs
# @main.route('/', defaults={'path': ''})
# @main.route('/<path:path>')
# def catch_all(path):
#     return render_template('not-found.html')