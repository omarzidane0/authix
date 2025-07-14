from flask import Flask , render_template ,redirect , Blueprint
from flask_jwt_extended import decode_token , create_access_token , JWTManager, jwt_required
from app.extensions import token_m
from flask_wtf.csrf import generate_csrf
home_bp = Blueprint("home" , __name__ , template_folder="templates" , static_folder="static" , static_url_path="/static-home")


@home_bp.route('/home')
@jwt_required()
def home():
    csrf = generate_csrf()
    return render_template("index.html" , csrf_token=csrf)

