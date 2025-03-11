from services.user_service import UserService
from flask import jsonify, make_response

class UserController:
    
    @staticmethod
    def signup(user_data):
        try:
            response = UserService.signup(user_data)
            res = make_response(jsonify({
                "accessToken" : response[0]
            }), 201)
            res.set_cookie(
               "jwt",
                response[1],
                httponly=True,
                secure=True,
                samesite="None",
                max_age=7 * 24 * 60 * 60  # 1 week 
            )
            return res
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)

    @staticmethod
    def login(user_data):
        try:
            response = UserService.login(user_data)
            res = make_response(jsonify({
                "accessToken" : response[0]
            }), 200)
            res.set_cookie(
               "jwt",
                response[1],
                httponly=True,
                secure=True,
                samesite="None",
                max_age=7 * 24 * 60 * 60  # 1 week 
            )
            return res
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
    
    @staticmethod
    def refresh(cookies):
        try:
            token = UserService.refreshToken(cookies)
            return jsonify({
                "accessToken" : token
            }), 200
        except Exception as e:
            return jsonify({
                "message": str(e)
            }), getattr(e, "statusCode", 400)
    
    @staticmethod
    def logout(cookies):
        try:
            if not cookies.get("jwt"):
                return "", 204
            res = make_response(jsonify({}), 204)
            res.delete_cookie("jwt", httponly=True, secure=True, samesite="None")
            return res
        except Exception as e:
            return jsonify({"message": str(e)}), getattr(e, "statusCode", 400)
    
    @staticmethod
    def get_profile():
        try:
            user = UserService.get_profile()
            return jsonify({
                "message": "User profile retrieved successfully",
                "user": user
                }), 200
        except Exception as e:
            return jsonify({"message": str(e)}), getattr(e, "statusCode", 400)