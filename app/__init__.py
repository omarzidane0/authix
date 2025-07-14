from flask import Flask , Blueprint
from app.routes.auth.login import login_bp
from app.routes.auth.register import register_bp
from app.routes.auth.otp import op_bp
from flask_sqlalchemy import SQLAlchemy
from app.extensions import db , csrf , token_m
from app.routes.home.home_p import home_bp
from app.config import Config
def create_app():
    app = Flask(__name__)
   # app.config["SECRET_KEY"] = "TESTING" # Change this!
    #app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///app.db"
    #app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
    #app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
    #app.config["JWT_COOKIE_SECURE"] = False 
    app.config.from_object(Config)
    db.init_app(app=app)
    csrf.init_app(app=app)
    token_m.init_app(app=app)
    app.register_blueprint(login_bp)
    app.register_blueprint(op_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(home_bp)
    from app.routes.auth.jwt_f import register_jwt_handlers
    register_jwt_handlers(token_m)
    return app