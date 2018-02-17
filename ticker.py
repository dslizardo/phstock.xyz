import requests
import threading
import json
import datetime
import redis_wrapper


HOST = 'http://www.pse.com.ph/stockMarket/home.html'
HEADERS = {'Referer': HOST}

redis = redis_wrapper.redis_client

def get_stocks():
    threading.Timer(10.0, get_stocks).start()
    r = requests.get(HOST+'?method=getSecuritiesAndIndicesForPublic&ajax=true', headers=HEADERS)
    stocks = r.json()

    for stock in stocks:
        redis.set('stocks:'+stock['securitySymbol'], stock)
    redis.set('stocks:all', stocks)
