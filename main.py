from flask import Flask
app = Flask(__name__)
import mainView

if __name__ == "__main__":
    app.add_url_rule('/', view_func=mainView.mainPage)
    app.run()