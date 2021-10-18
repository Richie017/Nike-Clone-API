import enum
from flask_sqlalchemy import SQLAlchemy

from . import db


class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    country = db.Column(db.String(40))
    color = db.Column(db.String(120), nullable=False)

    __tablename__ = 'person'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.name)


product_category = db.Table('product_categories',
                            db.Column('categories_id', db.Integer, db.ForeignKey(
                                'categories.id'), primary_key=True),
                            db.Column('product_id', db.Integer, db.ForeignKey(
                                'product.id'), primary_key=True)
                            )


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    imageURL = db.Column(db.String(200))
    category = db.relationship('categories', secondary=product_category,
                               lazy='subquery', backref=db.backref('product', lazy=True))
    status = db.Column(db.String(120), nullable=False)
    variants = db.relationship('product_variant', backref='product', lazy=True)
    tag = db.Column(db.String(120), nullable=False)
    #meta = db.Column(db.JSON)

    __tablename__ = 'product'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.name)


class ProductVariant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(100), nullable=False)
    size = db.Column(db.ARRAY(db.String(10)))
    regular_price = db.Column(db.Float())
    onsale = db.Column(db.Boolean())
    sales_price = db.Column(db.Float())
    product_id = db.Column(db.Integer, db.ForeignKey(
        'product.id'), nullable=False)

    __tablename__ = 'product_variant'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.product_id)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    main_category = db.Column(db.String(100), nullable=False)
    sub_category = db.Column(db.String(100), nullable=False)
    sub_sub_category = db.Column(db.String(100), nullable=False)

    __tablename__ = 'categories'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.main_category)


class GenderEnum(enum.Enum):
    male = 'male'
    female = 'female'


class NotificationEnum(enum.Enum):
    yes = 'yes'
    no = 'no'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    dob = db.Column(db.Date())
    gender = db.Column(db.Enum(GenderEnum))
    password = db.Column(db.String())
    country = db.Column(db.String(30))
    is_notification_enabled = db.Column(
        db.Enum(NotificationEnum), default=NotificationEnum.no)

    __tablename__ = 'user'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.first_name)


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.relationship('product', backref='cart', lazy=True)
    user = db.relationship('user', backref='cart', lazy=True)
    quantity = db.Column(db.Float())
    shipping_details = db.Column(db.JSON)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    __tablename__ = 'cart'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.product, self.user)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart = db.relationship('cart', backref='order', lazy=True)
    user = db.relationship('user', backref='order', lazy=True)
    total_price = db.Column(db.Float())
    payment_details = db.Column(db.JSON)
    order_status = db.Column(db.String(120), nullable=False)

    __tablename__ = 'order'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.cart, self.user)


favorite_products = db.Table('favorite_products',
                             db.Column('product_id', db.Integer, db.ForeignKey(
                                 'product.id'), primary_key=True),
                             db.Column('favorite_id', db.Integer, db.ForeignKey(
                                 'favorite.id'), primary_key=True)
                             )


class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product = db.relationship('product', secondary=favorite_products, lazy='subquery',
                              backref=db.backref('favorite', lazy=True))
    user = db.relationship('user', backref='favorite', lazy=True)

    __tablename__ = 'favorite'

    def __repr__(self):
        return '<id {}: {}>'.format(self.id, self.product, self.user)
