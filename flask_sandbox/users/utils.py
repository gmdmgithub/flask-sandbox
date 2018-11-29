import sys, secrets, os
from PIL import Image
from flask_mail import Message
from flask_sandbox import mail, app
from flask import url_for


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

def send_email(user):
    #print('email has been sent')
    token = user.generate_auth_token()
    message = Message('Reset Password',
            sender='noreplay@demo.com',
            recipients=[user.email])
    message.reply_to = "THIS IS THE EMAIL I WANT TO CHANGE@domain.com"
    message.body = f''' To reset your passwort visit that link
                    
    { url_for('users.reset_password',token=token, _external=True) }
                    
    Some dummy text here
    '''
    print('sending message to '+user.email)
    try:
        mail.send(message)
    except:
        print("Unexpected error:", sys.exc_info()[0])

