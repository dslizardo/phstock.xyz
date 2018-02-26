from . import redis_store
import requests
import threading
import json
import datetime
import decimal


HOST = 'http://www.pse.com.ph/stockMarket/home.html'
HEADERS = {'Referer': HOST}

def store_stocks():
    threading.Timer(60.0, store_stocks).start()
    print("Getting new stocks "+str(datetime.datetime.now()))
    r=requests.get(HOST+'?method=getSecuritiesAndIndicesForPublic&ajax=true', headers=HEADERS)
    stocks=r.json()
    for stock in stocks:
        redis_store.set('stocks:'+stock['securitySymbol'], json.dumps(stock))
    stocks=json.dumps(stocks)
    redis_store.set('stocks:all', stocks)
    top_gainers=get_top_gainers_or_losers(stocks, True)
    redis_store.set('stocks:top_gainers', json.dumps(top_gainers))
    top_losers=get_top_gainers_or_losers(stocks, False)
    redis_store.set('stocks:top_losers', json.dumps(top_losers))

    r=requests.get(HOST+'?method=getTopSecurity&limit=10&ajax=true', headers=HEADERS)
    most_active=r.json()
    redis_store.set('stocks:most_active', json.dumps(most_active))

def get_top_gainers_or_losers(json_data, flag):
    data=json.loads(json_data)
    sorted_data=sorted(data[1:], key=lambda x : decimal.Decimal(x['percChangeClose']), reverse=flag)
    return sorted_data[:10]
