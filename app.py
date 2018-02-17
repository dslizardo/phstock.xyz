from flask import Flask, json
import redis_wrapper
import ticker
app = Flask(__name__)

redis = redis_wrapper.redis_client

@app.route("/stocks")
def get_all_stocks():
    stocks=redis.get('stocks:all')
    return stocks

@app.route("/stock/<code>")
def get_stock(code):
    stock=redis.get('stocks:'+code)
    return stock

if __name__ == "__main__":
    ticker.get_stocks()
    app.run()
