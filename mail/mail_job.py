from . import mail
from flask_mail import Message
from pse import app, Stock
from flask import render_template
import schedule
import time

with app.app_context():
    def mail_job():
        active_stocks=Stock.get_stocks('most_active')
        winner_stocks=Stock.get_stocks('top_gainers')
        loser_stocks=Stock.get_stocks('top_losers')
        msg=Message('Test Subject 3',sender=app.config['FROM_SENDER'],  recipients = [app.config['TEST_RECIPIENT']])
        msg.html= render_template("stock_update.html", name="Daniel", active_stocks=active_stocks, winner_stocks=winner_stocks,loser_stocks=loser_stocks)
        mail.send(msg)

    schedule.every().day.at(app.config['SCHEDULED_MAIL']).do(mail_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
