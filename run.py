from flask import Flask
from app import create_app
from app import db

if __name__ == "__main__":
    app = create_app()
    from app.models.model import Accounts
    with app.app_context():
        db.create_all()
    app.run(debug=True)