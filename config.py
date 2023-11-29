import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
  DB_HOST = str(os.environ.get("DB_HOST"))
  DB_PORT = str(os.environ.get("DB_PORT"))
  DB_USERNAME = str(os.environ.get("DB_USERNAME"))
  DB_PASSWORD = str(os.environ.get("DB_PASSWORD"))
  DB_DATABASE = str(os.environ.get("DB_DATABASE"))

  JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET"))
  JWT_TOKEN_LOCATION = str(os.environ.get("JWT_TOKEN_LOCATION")).split(',')
  JWT_COOKIE_SECURE = str(os.environ.get("JWT_COOKIE_SECURE"))
  JWT_COOKIE_HTTPONLY = str(os.environ.get("JWT_COOKIE_HTTPONLY"))

  SECRET_KEY = str(os.environ.get("SECRET_KEY"))

  SQLALCHEMY_DATABASE_URI = 'postgresql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + ':' + DB_PORT + '/' + DB_DATABASE
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_RECORD_QUERIES = True

  UPLOAD_FOLDER = str(os.environ.get("UPLOAD_FOLDER"))
  MAX_CONTENT_LENGTH = 4 * 1024 * 1024

  TIMEZONE = str(os.environ.get("TIMEZONE"))