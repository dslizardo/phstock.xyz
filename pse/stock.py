from . import redis_store
import json

class Stock:
    def __init__(self, security_symbol, price, day_change ):
        self.security_symbol=security_symbol
        self.price=price
        self.day_change=day_change

    def get_stocks(key):
        data=json.loads(redis_store.get('stocks:'+key))
        if key == 'most_active':
            data=data['records']
        stocks=[]
        for stock in data:
            s=Stock(stock['securitySymbol'],stock['lastTradedPrice'],str(stock['percChangeClose'])+'%')
            stocks.append(s)
        return stocks
