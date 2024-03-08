import os

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Привет от приложения Flask"

@app.route("/index")
def index2():
    return "Привет от приложения Flask2"

if __name__ == '__main__':
    app.run()