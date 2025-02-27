from flask import request, g
from functools import wraps
import jwt
from datetime import datetime, timezone
from config import Config
from utils.error import AppError

def jwt_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or " " not in token:
            raise AppError("Forbidden", 403)

        try:
            token = token.split(" ")[1]
            decode = jwt.decode(token, Config.ACCESS_TOKEN_SECRET_KEY, algorithms=["HS256"])

            exp_str = decode.get("expiration")
            if exp_str:
                exp_datetime = datetime.strptime(exp_str, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=timezone.utc)
                
                if exp_datetime < datetime.now(timezone.utc):
                    raise AppError("Forbidden", 403)

            g.user = decode
            return f(*args, **kwargs)
        except Exception as e:
            print(e)
            raise AppError(getattr(e, 'message', "Unauthorized"), getattr(e, 'statusCode', 401))
    return wrapper
