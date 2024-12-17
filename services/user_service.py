from models.user import User
from utils.database import db
from werkzeug.security import generate_password_hash, check_password_hash

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
        if user and check_password_hash(user.password, data["password"]):
            return user
        return None
