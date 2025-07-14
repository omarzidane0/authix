from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_jwt_extended import JWTManager
db = SQLAlchemy()
token_m = JWTManager()
csrf =CSRFProtect()