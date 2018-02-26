from flask import json
from . import redis_store
from . import app

@app.route("/stocks")
def get_all_stocks():
    return redis_store.get('stocks:all')

@app.route("/stock/<code>")
def get_stock(code):
    return redis_store.get('stocks:'+code)

@app.route("/stocks/winners")
def get_winners():
    return redis_store.get('stocks:top_gainers')

@app.route("/stocks/losers")
def get_losers():
    return redis_store.get('stocks:top_losers')

@app.route("/stocks/active")
def get_most_active():
    return redis_store.get('stocks:most_active')
