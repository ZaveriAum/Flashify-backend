from flask import Blueprint
from .user_routes import user_blueprint

def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")
