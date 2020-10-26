import flaskApp
import mainView

import os

flaskApp.init()

meme_dir_path = os.path.join('static', 'meme_templates')
flaskApp.app.config['UPLOAD_FOLDER'] = meme_dir_path

if __name__ == "__main__":
    flaskApp.app.add_url_rule('/', view_func=mainView.mainPage)
    flaskApp.app.run()
