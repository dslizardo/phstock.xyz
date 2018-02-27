from flask import Flask
from flask_redis import FlaskRedis

# Load flask configurations
app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Initalize Redis
redis_store = FlaskRedis(app)

# Set Timer for Stock Update
from . import ticker
ticker.store_stocks()

# Initialize api endpoint
from . import routes

from .stock import Stock
# Initialize mail
from mail import mail_job
