from flask import Blueprint, request, jsonify
from controllers.user_controller import UserController

user_blueprint = Blueprint("user", __name__)
controller = UserController()

@user_blueprint.route("/signup", methods=["POSt"])
def get_folders():
    data = request.json
    return controller.signup(data)

@user_blueprint.route("/login", methods=["POST"])
def create_folder():
    data = request.json
    return controller.login(data)
