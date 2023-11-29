from flask import make_response, jsonify


def success(values, message):
    res = {
        "data": values,
        "message": message
    }

    return make_response(jsonify(res)), 200


def error(values, message):
    res = {
        "data": values,
        "message": message
    }

    return make_response(jsonify(res)), 400
