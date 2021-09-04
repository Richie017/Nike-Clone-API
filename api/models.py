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
