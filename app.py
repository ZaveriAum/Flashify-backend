from flask import Flask
from flask_cors import CORS
from utils.database import db, migrate
from routes import register_blueprints

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    
    CORS(app)
    db.init_app(app)
    migrate.init_app(app, db)

    register_blueprints(app)

    @app.route('/')
    def welcome():
        return "Welcome to Flashify"

    return app
    
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
