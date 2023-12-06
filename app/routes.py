
from flask_jwt_extended import jwt_required

from app import app, response
from app.controller import TicketController


@app.route('/ticket', methods=["GET"])
@jwt_required()
def index():
    return TicketController.index()


@app.route('/ticket/create', methods=["POST"])
@jwt_required()
def ticket():
    return TicketController.create()