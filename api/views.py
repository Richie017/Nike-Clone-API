from flask import Blueprint

from .models import People
from . import db, app


@app.route("/")
def index():
    print(People.query.all())
    return f"This is the API server for Nike-Clone Project developed by Potato Tech!"


@app.route("/db")
def data():
    return "Connected to db!"
