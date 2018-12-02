# flask-sandbox
Fisrt flask sandbox project
# instal flask
pip install Flask
# for env
pip install python-dotenv
# for secret you can use
$python
- $import secrets
- $secrets.token_hex(16)
# to catch all requests
At the end of the routs python file add:
- ``@app.route('/', defaults={'path': ''})``
- ``@app.route('/<path:path>')``
- ``def catch_all(path):``
   -  ``return render_template('not-found.html')``
# for database install
- $pip install flask-sqlalchemy
- from flask_sqlalchemy import SQLAlchemy : http://flask-sqlalchemy.pocoo.org/
# to create db
$python
- $from flask_sandbox import db
- $db.create_all()
- $from flask_sandbox.models import User, Post
- $usr = User(username='test',password='password',email='test@test.com')
- $db.session.add(usr) #add couple more 
- $db.session.commit()
- $User.query.all() # get the data
- $post = Post(....) #the same
# to create modules 
1. move files to the folder ie app (it would be a "package")
2. create file ```__init_.py``` and move configuration
3. in app.py (any main file) leave "from folder import app"
4. create routs.py to move routs and models.py to move model data
# hashing
* use bcrypt, for flask easier way is to: 
    * pip install flask-bcrypt
    * from flask_bcrypt import Bcrypt
    * bcrypt = Bcrypt()
    * bcrypt.generate_password_hash('test').decode('utf-8')
    * for stored password: bcrypt.check_password_hash(stored_pass,tested-password)
        * True or False
* add bcrypt to the ```__init__.py``` and use as other lib
# use LoginManager to user session management
All details can be found: https://flask-login.readthedocs.io/en/latest/
* most import feature - if you want to protect rout for login user, just add @login_required
    * if we add login_manager.login_view = 'login' we can simply use query parameter (next in this case)
    * import request module from flask
    * use as: request.args.get('next')
# Adding file from page
* First import file type filed from wft: ``from flask_wtf.file import FileField, FileAllowed``
* Add multipart to your form: ``enctype="multipart/form-data"``
* Add proper validation to the field ie: ``validators=[FileAllowed(['jpg','jpeg','png'])]``
* To get file extension: _f_name, f_ext = ``os.path.splitext(image.filename)``
* To resize image import Image from: ``from PIL import Image`` - first install: ``pip install Pillow`` and finally code like below:
    * output_size = (250, 250) #pixels
    * smal_image = Image.open(image)
    * smal_image.thumbnail(output_size)
    * smal_image.save(image_path) 
# Token validation
* Based on: https://blog.miguelgrinberg.com/post/restful-authentication-with-flask/page/4
* already included in flask (pip install itsdangerous)
* documentation: https://itsdangerous.palletsprojects.com/
* also JWT token in this lib
# Sending email
* For flask: https://pythonhosted.org/Flask-Mail/
* Update file ``__init__.py`` in main directory
# Create class form configuration
*  `` def create_app(config_class=Config):``
    ``app = Flask(__name__)``
    ``app.config.from_object(Config) ``
# Return JSON objects
* flask-marshmallow - is flask extension to integrate flask with marshmallow(an object serialization/deserialization library)
    * $ pip install flask_marshmallow
    * $ pip install marshmallow-sqlalchemy
    * in ``__init__.py``
        * from flask_marshmallow import Marshmallow
        * ma = Marshmallow()
        * ma.init_app(app)
    * ie for user clreate class:
        * `` class UserSchema(ma.Schema): ``
        `` class Meta: ``
                `` # Fields to expose``
                ``fields = ('username', 'email') ``
    * return in some routs like:
        * ``return user_schema.jsonify(user)``