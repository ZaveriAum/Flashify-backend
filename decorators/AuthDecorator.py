from flask import request
from functools import wraps
import jwt
from config import Config

def jwt_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers["Authorization"].split(" ")[1]
        if not token:
            print("token not there")
            raise Exception("User unauthorized")
        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            return f(*args, **kwargs)
        except Exception as e:
            raise Exception("User unauthorized")
    return wrapper