from pse import app
from flask_mail import Mail 

mail = Mail(app)

from . import mail_job
