from app import db
from datetime import datetime


class ts_team_support(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    team_code = db.Column(db.String(10), nullable=False, unique=True)
    team_name = db.Column(db.String(100), nullable=False)
    team_desc = db.Column(db.Text, nullable=True)
    team_status = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_team_support {}>'.format(self.team_name)
