from flask import Blueprint, request
from controllers.user_controller import UserController
from models.user import LoginSchema, SignupSchema
from decorators.RouteDecorator import validate_request

user_blueprint = Blueprint("user", __name__)
controller = UserController()

@user_blueprint.route("/signup", methods=["POST"], endpoint="signup_user")
@validate_request(SignupSchema)
def get_folders():
    data = request.json
    return controller.signup(data)

@user_blueprint.route("/login", methods=["POST"], endpoint="login_user")
@validate_request(LoginSchema)
def create_folder():
    data = request.json
    return controller.login(data)
