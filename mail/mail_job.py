from . import mail
from flask_mail import Message
from pse import app
import schedule
import time

with app.app_context():
    def mail_job():
        print(app.config['SEND_TO_EMAIL'])
        msg=Message('Test Subject 2',sender=app.config['FROM_SENDER'],  recipients = [app.config['TEST_RECIPIENT']])
        msg.body="Hello World"
        mail.send(msg)

    schedule.every().day.at(app.config['SCHEDULED_MAIL']).do(mail_job)

    while True:
        schedule.run_pending()
        time.sleep(1)
