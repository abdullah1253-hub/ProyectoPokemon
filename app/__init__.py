from flask import Flask
from flask_session import Session

def create_app():
    app = Flask(__name__)

    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = False
    app.config["SESSION_FILE_DIR"] = "./.flask_session"
    app.secret_key = "clave_super_secreta"

    Session(app)

    from app.routes.auth_routes import auth_bp
    from app.routes.pokemon_routes import pokemon_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(pokemon_bp)

    return app