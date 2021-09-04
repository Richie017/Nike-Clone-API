from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config.from_object(config.Config)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost/nike-clone"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views
