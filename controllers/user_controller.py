from services.user_service import UserService
from flask import jsonify

class UserController:
    
    @staticmethod
    def signup(user_data):
        try:
            user = UserService.signup(user_data)
            return jsonify({
                "status": True,
                "message": "Signed up successfully",
                "id": user.id,
                "username": user.username,
                "email": user.email,
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })

    @staticmethod
    def login(user_data):
        try:
            user = UserService.login(user_data)
            return jsonify({
                "status": True,
                "message": "Logged in successfully",
                "id": user.id,
                "username": user.username,
                "email": user.email,
            })
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            })
