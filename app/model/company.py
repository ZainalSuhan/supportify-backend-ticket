from app import db
from datetime import datetime


class ts_company(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    company_code = db.Column(db.String(10), nullable=False, unique=True)
    company_name = db.Column(db.String(200), nullable=False)
    company_description = db.Column(db.Text, nullable=True)
    company_address = db.Column(db.Text, nullable=True)
    company_province = db.Column(db.String(20), nullable=True)
    company_city = db.Column(db.String(20), nullable=True)
    company_district = db.Column(db.String(20), nullable=True)
    company_subdistrict = db.Column(db.String(20), nullable=True)
    company_postcode = db.Column(db.String(20), nullable=True)
    company_phone = db.Column(db.String(20), nullable=True)
    company_fax = db.Column(db.String(20), nullable=True)
    company_telephone = db.Column(db.String(20), nullable=True)
    company_mail = db.Column(db.String(100), nullable=True)
    company_website = db.Column(db.String(100), nullable=True)
    company_youtube = db.Column(db.String(100), nullable=True)
    company_fb = db.Column(db.String(100), nullable=True)
    company_x = db.Column(db.String(100), nullable=True)
    company_image = db.Column(db.String(200), nullable=True)
    company_favicon = db.Column(db.String(200), nullable=True)
    company_status = db.Column(db.Integer, nullable=True, default=0)
    created_date = db.Column(db.DateTime, default=datetime.now())
    created_by = db.Column(db.String(20), nullable=True)
    updated_date = db.Column(db.DateTime, default=datetime.now())
    updated_by = db.Column(db.String(20), nullable=True)

    def __repr__(self):
        return '<ts_company {}>'.format(self.company_name)
