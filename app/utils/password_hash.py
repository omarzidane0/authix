from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
import random
ps = PasswordHasher()

def hash_password(password):
    hashed_pass = ps.hash(password)
    return hashed_pass

def verify_password(password , hashedpass):
    return ps.verify(hashedpass , password)

def otp_generate():
    c = "abcdefghijklmnopqrstuvwxyz1234567890"
    lenth = 4 
    text= ""
    while(len(text)<4):
        text+=c[random.randint(0 , len(c)-1)]
    return text

if __name__ =="__main__":
    print(otp_generate())
    print(otp_generate())
    