from app.extensions import db

class Accounts(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String(60) , unique=True , nullable=False)
    email = db.Column(db.String(60) , unique=True , nullable=False)
    password = db.Column(db.String(60) , nullable=False)
    verified = db.Column(db.Boolean , default=False)
    def __init__(self , username , email , password):
        self.username = username
        self.email = email
        self.password = password
        

class user_otp(db.Model):
    id= db.Column(db.Integer , primary_key=True)
    user_id = db.Column(db.Integer , nullable=False)
    otp = db.Column(db.Integer)
    expiers_at = db.Column(db.DateTime)
    def __init__(self , user_id , otp , expiers_at):
        self.user_id = user_id
        self.otp = otp
        self.expiers_at = expiers_at