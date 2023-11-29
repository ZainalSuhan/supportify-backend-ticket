from app import db

class ts_temp_signup(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    account_code = db.Column(db.String(20), nullable=False, unique=True)
    account_username = db.Column(db.String(100), nullable=False)
    account_mail = db.Column(db.String(100), index=True, nullable=False, unique=True)
    account_password = db.Column(db.String(250), nullable=False)
    account_fullname = db.Column(db.String(100), nullable=False)
    otp = db.Column(db.String(6), index=True, nullable=False, unique=True)
    expired_time = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return '<ts_temp_signup {}>'.format(self.account_username)
    