from app import db

class ts_temp_signup(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    account_code = db.Column(db.String(20), nullable=True)
    account_username = db.Column(db.String(100), nullable=True)
    account_mail = db.Column(db.String(100), nullable=False)
    account_password = db.Column(db.String(250), nullable=True)
    account_fullname = db.Column(db.String(100), nullable=True)
    company_name = db.Column(db.String(200), nullable=False)
    otp = db.Column(db.String(6), nullable=True)
    expired_time = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return '<ts_temp_signup {}>'.format(self.account_username)
    