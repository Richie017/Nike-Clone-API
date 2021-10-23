from flask import Blueprint

from .models import Product, ProductVariant, Category, product_category
from . import db, app


@app.route("/")
def index():
    print(Product.query.all())
    return f"This is the API server for Nike-Clone Project developed by Potato Tech!"


@app.route("/db")
def data():
    return "Connected to db!"
