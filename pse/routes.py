from flask import jsonify
from . import app
from . import db
from .stock import Stock
from .response import Response
from .models.email import Email
from datetime import datetime
from validate_email import validate_email


@app.route("/stocks")
def get_all_stocks():
    stocks = Stock.get_stocks('all')
    return jsonify(Response("OK", stocks).__dict__)


@app.route("/stock/<code>")
def get_stock(code):
    stock = Stock.get_stock(code)
    return jsonify(Response("OK", stock).__dict__)


@app.route("/stocks/winners")
def get_winners():
    stocks = Stock.get_stocks('top_gainers')
    return jsonify(Response("OK", stocks).__dict__)


@app.route("/stocks/losers")
def get_losers():
    stocks = Stock.get_stocks('top_losers')
    return jsonify(Response("OK", stocks).__dict__)


@app.route("/stocks/active")
def get_most_active():
    stocks = Stock.get_stocks('most_active')
    return jsonify(Response("OK", stocks).__dict__)


@app.route("/subscribe/<email>")
def subscribe(email):
    if not validate_email(email):
        return jsonify("Email is not valid")
    email_exists =  Email.query.filter_by(email=email).first()
    if email_exists is not None:
        return jsonify("Email exists")
    register_email = Email(email=email, created_date=datetime.now())
    db.session.add(register_email)
    db.session.commit()
    return jsonify("OK")


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()
