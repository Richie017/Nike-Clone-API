from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "This is the API server for Nike-Clone Project created by Potato Tech!"
