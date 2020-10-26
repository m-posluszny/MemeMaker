from flask import *
import os

import flaskApp

def mainPage():
    full_img_path = os.path.join(flaskApp.app.config['UPLOAD_FOLDER'], 'Two-Buttons.jpg')
    return render_template('index.html', meme_img = full_img_path)

