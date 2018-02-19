import requests
import threading
import json
import datetime
import redis_wrapper
import decimal


HOST = 'http://www.pse.com.ph/stockMarket/home.html'
HEADERS = {'Referer': HOST}

redis = redis_wrapper.redis_client

def store_stocks():
    threading.Timer(10.0, store_stocks).start()
    r = requests.get(HOST+'?method=getSecuritiesAndIndicesForPublic&ajax=true', headers=HEADERS)
    stocks = r.json()
    for stock in stocks:
        redis.set('stocks:'+stock['securitySymbol'], json.dumps(stock))
    redis.set('stocks:all', json.dumps(stocks))
    top_gainers=get_top_gainers(json.dumps(stocks))
    redis.set('stocks:top_gainers', top_gainers)

def get_top_gainers(json_data):
    data=json.loads(json_data)
    sorted_data=sorted(data[1:], key=lambda x : decimal.Decimal(x['percChangeClose']), reverse=True)
    return sorted_data[:10]
