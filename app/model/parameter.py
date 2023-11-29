from app import db
from datetime import datetime


class ts_parameter(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    param_code = db.Column(db.String(10), nullable=False, unique=True)
    param_name = db.Column(db.String(100), nullable=False)
    param_status = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_parameter {}>'.format(self.param_name)
