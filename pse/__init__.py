from flask import Flask
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from .models.base import db

# Load flask configurations
app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Initialize Databas
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(password)s@%(host)s:%(port)s/%(db)s' % app.config['POSTGRES']

db.init_app(app)

# Initalize Redis
redis_store = FlaskRedis(app)

# Set Timer for Stock Update
from . import ticker

ticker.store_stocks()
# Get latest stocks at first run
ticker.retrieve_stocks()

# Initialize api endpoint
from . import routes

from .stock import Stock
# Initialize mail
from mail import mail_job
