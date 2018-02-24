from flask import json
from . import redis_wrapper
from . import app

redis = redis_wrapper.redis_client

@app.route("/stocks")
def get_all_stocks():
    return redis.get('stocks:all')

@app.route("/stock/<code>")
def get_stock(code):
    return redis.get('stocks:'+code)

@app.route("/stocks/winners")
def get_winners():
    return redis.get('stocks:top_gainers')

@app.route("/stocks/losers")
def get_losers():
    return redis.get('stocks:top_losers')

@app.route("/stocks/active")
def get_most_active():
    return redis.get('stocks:most_active')
