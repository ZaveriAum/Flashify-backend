from flask import Blueprint
from .user_routes import user_blueprint
from .folder_routes import folder_blueprint

def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(folder_blueprint, url_prefix="/folder")
