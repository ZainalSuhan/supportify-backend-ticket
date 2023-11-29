from app import db
from datetime import datetime


class ts_ticket_message(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    ticket_no = db.Column(db.String(10), nullable=False, unique=True)
    message_from = db.Column(db.String(20), nullable=False)
    message_to = db.Column(db.String(20), nullable=False)
    message_subject = db.Column(db.String(100), nullable=False)
    message_description = db.Column(db.Text, nullable=False)
    message_attachment = db.Column(db.String(200), nullable=False)
    message_date = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<ts_ticket_message {}>'.format(self.ticket_no)
