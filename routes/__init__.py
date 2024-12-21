from flask import Blueprint
from .user_routes import user_blueprint
from .folder_routes import folder_blueprint
from .flashcard_routes import flashcard_blueprint
from .ai_routes import ai_blueprint

def register_blueprints(app):
    app.register_blueprint(user_blueprint, url_prefix="/user")
    app.register_blueprint(folder_blueprint, url_prefix="/folder")
    app.register_blueprint(flashcard_blueprint, url_prefix="/flashcard")
    app.register_blueprint(ai_blueprint, url_prefix="/ai")
