from .base import db

class Email(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(320), unique=True, nullable=False)
    created_date = db.Column(db.TIMESTAMP)

    def __repr__(self):
        return '<Email %r>' % (self.email)
