🛡️ Secure Login Panel using Flask & JWT
This project is a modern and secure authentication panel built with Flask. It includes user Login, Registration, and Email Verification via OTP. The system leverages JSON Web Tokens (JWT) for secure session management.

✅ Features:
User registration and login using email and password.

OTP (One-Time Password) sent to the user's email for account verification.

Passwords are securely hashed using Argon2.

Session management using JWT (access and refresh tokens).

Protection against CSRF attacks.

Clean and modular project structure.

🧰 Tech Stack:
Flask & Flask_SQLAlchemy for backend logic and ORM.

Flask_WTF & CSRFProtect for form validation and CSRF protection.

flask_jwt_extended for token generation and management.

smtplib & email.message for sending OTP emails.

argon2 for password hashing.

datetime & random for OTP expiration and generation.

💡 Possible Future Enhancements:
Social login (Google, GitHub, etc.).

Forgot/Reset password functionality.

Frontend integration with React or Vue.

Admin/user dashboards.
