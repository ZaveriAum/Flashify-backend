from services.user_service import UserService
from flask import jsonify

class UserController:
    
    @staticmethod
    def signup(user_data):
        try:
            user = UserService.signup(user_data)
            return jsonify({
                "status": True,
                "message": "signed up successfully",
            }), 201
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400

    @staticmethod
    def login(user_data):
        try:
            response = UserService.login(user_data)
            return jsonify({
                "status": True,
                "message": "Logged in successfully",
                "id": response[0].id,
                "username": response[0].username,
                "email": response[0].email,
                "token": response[1],
            }), 200
        except Exception as e:
            return jsonify({
                "status": False,
                "message": str(e)
            }), 400
