from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class ts_account(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    account_code = db.Column(db.String(20), nullable=False, unique=True)
    account_username = db.Column(db.String(100), nullable=False)
    account_password = db.Column(db.String(250), nullable=False)
    account_fullname = db.Column(db.String(100), nullable=False)
    account_mail = db.Column(db.String(100), index=True, nullable=False, unique=True)
    account_phone = db.Column(db.String(20), nullable=True, unique=True)
    privilege_code = db.Column(db.String(10), nullable=True, unique=True)
    company_code = db.Column(db.String(10), nullable=True, unique=True)
    client_code = db.Column(db.String(10), nullable=True, unique=True)
    departement_code = db.Column(db.String(10), nullable=True, unique=True)
    team_code = db.Column(db.String(10), nullable=True, unique=True)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_account {}>'.format(self.account_username)

    def setPassword(self, account_password):
        self.account_password = generate_password_hash(account_password)

    def checkPassword(self, account_password):
        return check_password_hash(self.account_password, account_password)
