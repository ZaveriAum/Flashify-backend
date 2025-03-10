from flask import request, jsonify
from functools import wraps
from config import Config
from marshmallow import ValidationError

def validate_request(schema):
    def route_validator(f):
        def wrapper(*args, **kwargs):
            try:
                data = request.json
                schema().load(data)
                return f(*args, **kwargs)
            except ValidationError as err:
                first_error_message = next((message[0] for message in err.messages.values() if message), None)
                return jsonify({"message": first_error_message}), 400
        return wrapper
    return route_validator