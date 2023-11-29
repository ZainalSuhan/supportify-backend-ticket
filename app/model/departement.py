from app import db
from datetime import datetime


class ts_departement(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    departement_code = db.Column(db.String(10), nullable=False, unique=True)
    departement_name = db.Column(db.String(100), nullable=False)
    departement_desc = db.Column(db.Text, nullable=True)
    departement_status = db.Column(db.Integer, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_departement {}>'.format(self.departement_name)
