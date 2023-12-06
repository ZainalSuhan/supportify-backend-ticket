from app import db
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB


class ts_ticket(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    ticket_no = db.Column(db.String(10), nullable=False, unique=True)
    ticket_subject = db.Column(db.String(250), nullable=False)
    ticket_type = db.Column(db.String(10), nullable=False)
    ticket_status = db.Column(db.String(10), nullable=False)
    ticket_priority = db.Column(db.String(10), nullable=False)
    ticket_author = db.Column(db.String(20), nullable=False)
    ticket_assignee = db.Column(db.String(20), nullable=False)
    ticket_start_date = db.Column(db.DateTime, default=datetime.now())
    ticket_finish_date = db.Column(db.DateTime, nullable=True)
    ticket_estimed_time = db.Column(db.Integer, default=0)
    ticket_progress = db.Column(db.Integer, default=1)
    ticket_desc = db.Column(db.Text)
    ticket_attachment = db.Column(JSONB, nullable=True)
    departement_code = db.Column(db.String(10), nullable=False)
    submission_date = db.Column(db.DateTime, default=datetime.now())
    submission_by = db.Column(db.String(20), nullable=True)
    process_date = db.Column(db.DateTime, default=datetime.now())
    process_by = db.Column(db.String(20), nullable=True)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, nullable=True)
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_ticket {}>'.format(self.ticket_no)
