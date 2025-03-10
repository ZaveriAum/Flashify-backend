from flask import Blueprint, request
from controllers.user_controller import UserController
from models.user import LoginSchema, SignupSchema
from decorators.RouteDecorator import validate_request

user_blueprint = Blueprint("user", __name__)
controller = UserController()

@user_blueprint.route("/signup", methods=["POST"], endpoint="signup_user")
@validate_request(SignupSchema)
def signup():
    data = request.json
    return controller.signup(data)

@user_blueprint.route("/login", methods=["POST"], endpoint="login_user")
@validate_request(LoginSchema)
def login():
    data = request.json
    return controller.login(data)

@user_blueprint.route("/refresh", methods=["GET"], endpoint="refresh_token")
def refresh():
    cookies = request.cookies
    return controller.refresh(cookies)

@user_blueprint.route("/logout", methods=["POST"], endpoint="logout")
def logout():
    cookies = request.cookies
    return controller.logout(cookies)

@user_blueprint.route("/profile", methods=["GET"], endpoint="profile")
def profile():
    return controller.get_profile()
