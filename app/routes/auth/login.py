from flask import Flask , Blueprint , render_template , url_for, request , jsonify , session , redirect , make_response
from flask_sqlalchemy import SQLAlchemy
from app.models.model import Accounts
from app.extensions import db
from app.utils.password_hash import verify_password
from flask_jwt_extended import unset_jwt_cookies, create_access_token , decode_token , set_access_cookies ,verify_jwt_in_request ,get_jwt_identity
login_bp = Blueprint("login", __name__ , template_folder="templates" , static_folder="static" , static_url_path="/stsatic-login")

@login_bp.route("/login" , methods=["POST" , "GET"])
def login():
    try:
        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()
        if user_id:
            return redirect("/home")
        else:
            return render_template("login.html")
    except:
        return render_template("login.html")

@login_bp.route("/login-post" , methods=["POST"])
def login_post():
    data = request.get_json()
    if data["username"] == "" or data["password"]=="":
        return jsonify({'status':False , 'reason':'please fill alll the blanks'})
    user = Accounts.query.filter_by(username=data["username"])
    if user.count() > 0:
        try:
            verify_password(data['password'],user.first().password )
            if user.first().verified == False:
                session["user_v"] = user.first().id
                response = make_response(jsonify({'status':True , "link":"/verify_otp"}))
                return response
            else:
                token = create_access_token(identity=str(user.first().id))
                response = make_response(jsonify({'status':True , "link":"/home"}))
                set_access_cookies(response , token)
                return response
        except:
            return jsonify({'status':False , 'reason':'Wrong Username Or Password'})
    else:
        return jsonify({'status':False , 'reason':'Wrong Username Or Password'})
    

@login_bp.route("/logout" , methods=["POST"])
def log_out():
    try:
        verify_jwt_in_request(optional=True)
        user_id = get_jwt_identity()
        if user_id:
            response = make_response(redirect("/login"))
            unset_jwt_cookies(response=response)
            return response
        else:
            return redirect("/login")
    except:
        response = make_response(redirect("/login"))
        unset_jwt_cookies(response=response)
        return response

