import sys, secrets, os
from PIL import Image
from flask_mail import Message
from flask_sandbox import mail, logging
from flask import url_for, current_app
from flask_sandbox.models import User

import folium
from flask_sandbox.config_app import Config

def save_image(image:Image):
    random_hex = secrets.token_hex(8)
    _f_name, f_ext = os.path.splitext(image.filename) #when you do not use variable  start it _ 
    image_filename = random_hex+f_ext
    image_path = os.path.join(current_app.root_path,'static/profile_img',image_filename)
    
    output_size = (250, 250)
    i = Image.open(image)
    i.thumbnail(output_size)
    i.save(image_path)
    logging.info(f'file saved {image_filename}')
    
    return image_filename

def send_email(user:User):
    #print('email has been sent')
    token = user.generate_auth_token()
    message = Message(r'Reset Password',
            sender='noreplay@demo.com',
            recipients=[user.email])
    message.reply_to = "THIS IS THE EMAIL I WANT TO CHANGE@domain.com"
    message.body = f''' To reset your passwort visit that link
                    
    { url_for('users.reset_password',token=token, _external=True) }
                    
    Some dummy text here
    '''
    #print('sending message to '+user.email)
    logging.info(f'Sending email to {user.email}')
    try:
        mail.send(message)
    except:
        logging.error(f"Unexpected error: {sys.exc_info()[0]}" )
        #print(r"Unexpected error:", sys.exc_info()[0]) #print r - raw string, thanks fot that you have not modified

def generate_map():
    if not Config.map_created:
        try:
            map = folium.Map(location=[50.062379, 19.936971], zoom_start=6)
            file_name = Config.main_path+"\\templates\\map.html"
            map.save(file_name)    
            logging.info(f'Map file to save: {file_name}')
            Config.map_created = True
        except Exception as e:
            logging.error(str(e))
            #print(e)        
        
    

