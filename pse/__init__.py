from flask import Flask
from . import ticker

app = Flask(__name__)
ticker.store_stocks()
from . import routes
