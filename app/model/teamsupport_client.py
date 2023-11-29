from app import db
from datetime import datetime


class ts_team_support_client(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    team_code = db.Column(db.String(10), nullable=False, unique=True)
    company_code = db.Column(db.String(10), nullable=False, unique=True)
    client_code = db.Column(db.String(10), nullable=False, unique=True)
    account_code = db.Column(db.String(10), nullable=False, unique=True)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_team_support_client {}>'.format(self.id)
