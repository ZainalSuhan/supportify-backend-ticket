from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt_header

from app import app, response
from app.controller import OTPController
from app.controller import SignupController, SigninController, SignoutController
from app.handler import is_token_blacklisted


@app.route('/register', methods=["POST"])
def funcRegister():
    return SignupController.register()


# @app.route('/otp', methods=["GET"])
# def otp():
#     return OTPController.otp()


@app.route('/validate-otp', methods=["POST"])
def validate():
    return OTPController.validate()


@app.route('/login', methods=["POST"])
def funcSignin():
    return SigninController.login()


@app.route('/logout', methods=["POST"])
@jwt_required()
def funcSignout():
    current_user = get_jwt_identity()
     
    access_token = get_jwt_header()

    if not is_token_blacklisted(access_token, current_user):
        return SignoutController.logout()
    else:
        return response.error(401, 'Token has been revoked')

@app.route('/ticket', methods=["GET"])
@jwt_required()
def ticket():
  current_user = get_jwt_identity()

  # Mengecek apakah token berada dalam daftar hitam
  access_token = get_jwt_header()

  if is_token_blacklisted(access_token, current_user):
    return response.error(401, 'Token has been revoked')

  return f"Hello, this is ticket page! I'm access this page as {current_user}"
