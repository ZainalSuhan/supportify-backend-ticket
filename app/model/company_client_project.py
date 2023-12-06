from app import db
from datetime import datetime


class ts_company_client_project(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    client_code = db.Column(db.String(10), nullable=False)
    project_code = db.Column(db.String(10), nullable=False)
    project_name = db.Column(db.String(100), nullable=False)
    desc = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_company_client_project {}>'.format(self.client_name)
    