from app import db

class ts_temp_signin(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    account_mail = db.Column(db.String(100), nullable=False)
    account_password = db.Column(db.String(250), nullable=False)
    otp = db.Column(db.String(6), nullable=False)
    expired_time = db.Column(db.DateTime, nullable=False)
    
    def __repr__(self):
        return '<ts_temp_signin {}>'.format(self.account_mail)
    