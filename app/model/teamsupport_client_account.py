from app import db
from datetime import datetime


class ts_team_support_client_account(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    team_code = db.Column(db.String(10), nullable=False)
    account_code = db.Column(db.String(10), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_team_support_client_account {}>'.format(self.id)
    