import os
import redis
import smtplib
from datetime import datetime

from app import app, jwt
from minio import Minio
from elasticsearch import Elasticsearch
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def elastic_init():
    es = Elasticsearch([str(os.environ.get("ELASTIC_URI"))])

    return es


def redis_init():
    re = redis.StrictRedis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
                                            db=app.config['REDIS_DB'])

    return re


def minio_init():
    minio_endpoint = str(os.environ.get("MINIO_ENDPOINT"))
    minio_access_key = str(os.environ.get("MINIO_ACCESS_KEY"))
    minio_secret_key = str(os.environ.get("MINIO_SECRET_KEY"))

    minio = Minio(minio_endpoint, access_key=minio_access_key, secret_key=minio_secret_key, secure=False)

    return minio


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    jwt_redis_blocklist = redis_init()
    token_in_redis = jwt_redis_blocklist.get(jti)
    return token_in_redis is not None


def generate_sequence(model=None, code_attribute='', prefix=''):
    last_record = model.query.order_by(model.id.desc()).first()

    if last_record:
        last_sequence = getattr(last_record, code_attribute, '')
        last_number_str = ''.join(filter(str.isdigit, last_sequence))
        last_number = int(last_number_str) if last_number_str else 0
        sequence_number = last_number + 1
    else:
        sequence_number = 1

    new_sequence = f'{prefix}{sequence_number:04}'
    return new_sequence


def send_email(subject, body, recipients):
    sender = app.config['MAIL_USERNAME']
    password = app.config['MAIL_PASSWORD']

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ', '.join(recipients)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'html'))

    try:
        server = smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT'])
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, recipients, message.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
