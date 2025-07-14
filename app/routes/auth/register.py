from flask import Flask , Blueprint , render_template , request ,jsonify , session , redirect , url_for
from app.models.model import Accounts , user_otp
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import verify_jwt_in_request , get_jwt_identity
from app.utils.password_hash import hash_password , verify_password
from app.models.model import db
register_bp = Blueprint("register" , __name__ , template_folder="templates" , static_folder="static" , static_url_path="/static-register")
#start from here tommorow
@register_bp.route("/register" , methods=["GET" , "POST"])
def register():
    try:
        verify_jwt_in_request(optional=True)
        print("here")
        user_id = get_jwt_identity()
        print(user_id)
        if user_id:
            return redirect("/home")
        else:
            return render_template("register.html")
    except:
        return render_template("register.html")

@register_bp.route("/register-post" , methods=["POST"])
def register_p():
    data = request.get_json()
    print(data['username'])
    if data['username'] == "" or data['email'] == "" or data['password'] == "":
        return jsonify({'status':False , 'reason':"please fill all blanks"})
    if Accounts.query.filter_by(username=data['username']).count() > 0:
        return jsonify({'status':False , "reason":"username existed"})
    if Accounts.query.filter_by(email=data['email']).count() > 0:
        return jsonify({'status':False , "reason":"email already used"})
    passw = hash_password(data['password'])
    user = Accounts(username = data['username'] ,email =  data['email'] , password = passw)
    db.session.add(user)
    db.session.commit()
    session["user_v"] = Accounts.query.filter_by(username=data['username']).first().id
    return jsonify({'status' : True , 'link':'/verify_otp' })