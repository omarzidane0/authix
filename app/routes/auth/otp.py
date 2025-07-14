from flask import Flask , Blueprint , render_template , request ,jsonify , session , redirect , url_for , make_response
from app.models.model import Accounts , user_otp
from flask_sqlalchemy import SQLAlchemy
from app.models.model import db
from app.utils.email_sender import send_email
from app.utils.password_hash import otp_generate
from datetime import datetime, timedelta
from flask_wtf.csrf import generate_csrf
from flask_jwt_extended import create_access_token , decode_token , set_access_cookies ,verify_jwt_in_request

op_bp = Blueprint("op" , __name__ , template_folder="templates")


@op_bp.route("/verify_otp" , methods=["POST", "GET"])
def verify_otp():
    csrf = generate_csrf()
    if "user_v" in session:
        if request.method == "POST":
            r_otp = request.form.get("otp")
            print(r_otp)
            print(session['user_v'])
            print("this is the status")
            if r_otp == "":
                return render_template("otp.html" , warn="Alert : INPUT IS EMPTY" , csrf_token=csrf)
            otp_user = user_otp.query.filter_by(user_id = session["user_v"] , otp=r_otp).first()
            print(otp_user)
            if otp_user != None:
              
                if otp_user.expiers_at > datetime.utcnow():
                    token = create_access_token(identity=str(session["user_v"]))
                    print(token)
                    user = Accounts.query.filter_by(id=session["user_v"]).first()
                    print("here")
                    user.verified = True
                    db.session.commit()
                    print("here2")
                    user_otp.query.filter_by(user_id = session["user_v"] , otp=r_otp).delete()
                    db.session.commit()
                    response = make_response(redirect("/home"))
                    session.pop("user_v", None)
                    print("here end")
                    set_access_cookies(response , token)
                    return response
                    # give access token // turn to home page
                else:
                    db.session.delete(otp_user)
                    db.session.commit()
                    return render_template("otp.html" , warn="Alert : expierd OTP" , csrf_token=csrf)
            else:
                 return render_template("otp.html" , warn="Alert : Wrong OTP", csrf_token=csrf)
        us_a = Accounts.query.filter_by(id= session["user_v"])
        if us_a.count() == 0:
            return redirect("/login")
        # add the access later
        if us_a.first().verified == True:
            return redirect("/home")
        uso = user_otp.query.filter_by(user_id = session["user_v"])
        if uso.count() > 0 and datetime.utcnow() < uso.first().expiers_at:
            return render_template("otp.html", csrf_token=csrf)
        if uso.count() > 0 and datetime.utcnow() > uso.first().expiers_at:
            uso.delete()
            db.session.commit()
        otp = otp_generate()
        user_ot = user_otp(session["user_v"]  , otp , datetime.utcnow() + timedelta(minutes=1) )
        db.session.add(user_ot)
        db.session.commit()
        user = Accounts.query.filter_by(id=session["user_v"]).first()
        send_email(user.email , "Your OTP Code !!" , f"{otp}")
        return render_template("otp.html", csrf_token=csrf)
    else:
        # اذا معها اكسس توكن حوله لصفحة الرئيسي
        # مامعه اكسس توكن ومامعه السشن ايدي رجع ل تعريص الوجن خليه يتعرص من هناك
        try:
            verify_jwt_in_request() 
            print("directing to home")
            return redirect("/home")
        except:
            print("directing to login page")
            return redirect("/login")