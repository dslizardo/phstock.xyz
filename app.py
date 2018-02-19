from flask import Flask, json
import redis_wrapper
import ticker
app = Flask(__name__)

redis = redis_wrapper.redis_client

@app.route("/stocks")
def get_all_stocks():
    return redis.get('stocks:all')

@app.route("/stock/<code>")
def get_stock(code):
    return redis.get('stocks:'+code)

@app.route("/stocks/top-gainers")
def get_top_gainers():
    return redis.get('stocks:top_gainers')

if __name__ == "__main__":
    ticker.store_stocks()
    app.run()
