from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask_mail import Message
from flask import render_template
from pse import app, Stock
from . import mail
from datetime import datetime


def mail_job():
    active_stocks = Stock.get_stocks('most_active')
    winner_stocks = Stock.get_stocks('top_gainers')
    loser_stocks = Stock.get_stocks('top_losers')
    with app.app_context():
        date=datetime.now()
        msg = Message(date.strftime('Market Summary %b %d, %Y'), sender=app.config['FROM_SENDER'], recipients=[app.config['TEST_RECIPIENT']])
        msg.html = render_template("stock_update.html", name="Daniel", active_stocks=active_stocks,
                                   winner_stocks=winner_stocks, loser_stocks=loser_stocks)
        mail.send(msg)


scheduler = BackgroundScheduler()

scheduler.add_job(mail_job, CronTrigger.from_crontab(app.config['MAIL_CRON']))
scheduler.start()
