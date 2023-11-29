from app import db
from datetime import datetime


class ts_sla(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    ticket_type = db.Column(db.String(10), nullable=False)
    ticket_status = db.Column(db.String(10), nullable=False)
    ticket_priority = db.Column(db.String(10), nullable=False)
    estimated_days = db.Column(db.Integer, default=1)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_sla {}>'.format(self.id)
