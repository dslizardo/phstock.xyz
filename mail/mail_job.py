from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask_mail import Message
from flask import render_template
from pse import app, Stock
from . import mail
import time

def mail_job():
    active_stocks=Stock.get_stocks('most_active')
    winner_stocks=Stock.get_stocks('top_gainers')
    loser_stocks=Stock.get_stocks('top_losers')
    with app.app_context():
        msg=Message('Test Subject 3',sender=app.config['FROM_SENDER'],  recipients = [app.config['TEST_RECIPIENT']])
        msg.html= render_template("stock_update.html", name="Daniel", active_stocks=active_stocks, winner_stocks=winner_stocks,loser_stocks=loser_stocks)
        mail.send(msg)

scheduler = BackgroundScheduler()

scheduler.add_job(mail_job, CronTrigger.from_crontab('30 17 * * 1-5'))
scheduler.start()
