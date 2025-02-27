from models.user import User
from utils.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
import jwt
from datetime import datetime, timedelta 
from config import Config
from utils.error import AppError

class UserService:

    @staticmethod
    def generateToken(email):
        try:
            accessToken = jwt.encode({
                        'email': email,
                        'expiration': str(datetime.utcnow() + timedelta(seconds=3600)) # one hour
                    },
                    Config.ACCESS_TOKEN_SECRET_KEY)
            
            refreshToken = jwt.encode({
                        'email': email,
                        'expiration': str(datetime.utcnow() + timedelta(seconds=3600 * 24 * 7)) # one week
                    },
                    Config.REFRESH_TOKEN_SECRET_KEY)
            return (accessToken, refreshToken)
        except Exception as e:
            raise AppError('Internal Server Error', 500)
    
    @staticmethod
    def signup(user):
        try:
            if UserService.get_user_by_email(user['email']):
                raise AppError("User already exists", 400)
            hashed_password = generate_password_hash(user["password"])
            new_user = User(username=user["username"], email=user["email"], password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return UserService.generateToken(user["email"])
        except Exception as e:
            print(e)
            raise AppError(getattr(e, "message", "Unknown Error"), getattr(e, "statusCode", 500))
    
    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()


    @staticmethod
    def login(data):
        try:
            user = UserService.get_user_by_email(data["email"])
            if user != None:
                if check_password_hash(user.password, data["password"]):
                    return UserService.generateToken(email=data["email"])
                else:
                    raise ValueError("Invalid credentials")
            raise ValueError("User does not exists.")
        except Exception as e:
            raise AppError(getattr(e, "message", "Unknown Error"), getattr(e, "statusCode", 500))
    
    @staticmethod
    def refreshToken(cookies):
        try:
            if not cookies.get("jwt"):
                raise AppError('Forbidden', 403)
            refreshToken = cookies.get("jwt");
            decode = jwt.decode(refreshToken, Config.REFRESH_TOKEN_SECRET_KEY, algorithms=["HS256"])
            user = UserService.get_user_by_email(decode['email'])
            if not user:
                raise AppError('Unauthorized', 401)
            
            return jwt.encode({
                            'email': user.email,
                            'expiration': str(datetime.utcnow() + timedelta(seconds=3600 * 24 * 7)) # one week
                        },
                        Config.REFRESH_TOKEN_SECRET_KEY)
        except Exception as e:
            raise AppError(getattr(e, "message", "Unknown Error"), getattr(e, "statusCode", 500))

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
