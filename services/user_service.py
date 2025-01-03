from models.user import User
from utils.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token
import jwt
from datetime import datetime, timedelta 
from config import Config

class UserService:

    @staticmethod
    def signup(user):
        hashed_password = generate_password_hash(user["password"])
        new_user = User(username=user["username"], email=user["email"], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_user_by_email(email):
        return User.query.filter_by(email=email).first()


    @staticmethod
    def login(data):
        user = UserService.get_user_by_email(data["email"])
        if user != None:
            if check_password_hash(user.password, data["password"]):
                token = jwt.encode({
                    'email': data["email"],
                    'expiration': str(datetime.utcnow() + timedelta(seconds=3600))
                },
                Config.JWT_SECRET_KEY)
                return (user, token)
            else:
                raise ValueError("Invalid credentials")
        raise ValueError("User does not exists.")

    @staticmethod
    def get_user_by_id(user_id):
        return User.query.get(user_id)
