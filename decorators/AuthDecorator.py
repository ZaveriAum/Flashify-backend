from flask import request
from functools import wraps
import jwt
from config import Config
from utils.error import AppError

def jwt_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        if not token:
            raise AppError("Forbiden", 403)
        try:
            data = jwt.decode(token, Config.ACCESS_TOKEN_SECRET_KEY, algorithms=["HS256"])
            return f(*args, **kwargs)
        except Exception as e:
            raise AppError("Unuathorized", 401)
    return wrapper
