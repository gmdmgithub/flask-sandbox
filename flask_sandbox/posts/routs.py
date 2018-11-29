from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
import secrets
from PIL import Image
from flask_login import current_user, login_required
from flask_sandbox.posts.forms import EditPostForm
from flask_sandbox.models import Post
from flask_sandbox.config import new_post_p, post_p
from flask_sandbox import db

posts = Blueprint('posts',__name__)

#rout for post
@posts.route('/post/new',methods=['GET','POST'])
@login_required
def new_post():
    form = EditPostForm()
    if form.validate_on_submit():
        #post = Post(title=form.title.data,content=form.content.data,user_id=current_user.id)
        post = Post(title=form.title.data,content=form.content.data,author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(f'Your post has been created!!', 'success')
        return redirect(url_for('main.home'))
    return render_template('edit_post.html',param=new_post_p, form=form, mode='new')


#rout for post
@posts.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    if not 'static' in post.author.image_file:
        post.author.image_file = "/static/profile_img/"+post.author.image_file
    return render_template('post.html',param=post_p, post=post)

#rout for post
@posts.route('/post/<int:post_id>/update',methods=['GET','POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = EditPostForm()  
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data 
        db.session.commit()
        flash(f'Your post has been updated', 'success')
        return redirect(url_for('posts.post',post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('edit_post.html',param=new_post_p, form=form, mode='edit')


@posts.route('/post/<int:post_id>/delete',methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash(f'Your post has been deleted', 'success')
    return redirect(url_for('main.home'))