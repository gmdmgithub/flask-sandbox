from flask import Flask, render_template, url_for, flash, redirect
from reg_form import RegistrationForm
from login_form import LoginForm
from os.path import join, dirname
import os
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")

app = Flask(__name__)

app.config['SECRET_KEY'] = SECRET_KEY

#lets add some posted data (simply not from db)

post = [
    {
        'author': 'John Doe',
        'title': 'My best friend',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-01-15'
    },
    {
        'author': 'Janet Jecson',
        'title': 'My brother',
        'content': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Officia incidunt aperiam ut distinctio doloremque. Illo maxime soluta dolore dolorem tempore.',
        'post_date': '2018-02-15'
    }
]

home ={
    'active':'home',
    'title' : 'Home page'
}
about ={
    'active':'about',
    'title' : 'About page'
}

register = {
    'active':'registration',
    'title': 'Registration page'
}

login = {
    'active':'login',
    'title': 'Login page'
}

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',param=home, postList=post) #"<h1>Hi there - here is flask - no restart</h1>"

#anbout page
@app.route("/about")
def about():
    return render_template('about.html', param=about, title="About page")

#route for registration form
@app.route('/register',methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', param=register, form=form)

#route login form
@app.route('/login',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login to the system {form.username.data}!','success')


#not foud - bed address
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template('not-found.html')
    return redirect(url_for('home'))
return render_template('login.html', param=login, form=form)


if __name__ == "__main__":
    app.run(debug=True)
