from flask import Flask

def init():
    global app
    app = Flask(__name__)

