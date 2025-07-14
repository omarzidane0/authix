from flask import Flask , redirect , render_template_string , Blueprint

def register_jwt_handlers(jwt):

    @jwt.unauthorized_loader
    def missing_token_callback(err_msg):
        print("NO TOKEN!")
        return render_template_string("""
            <script>window.location.href = "/login";</script>
        """), 401

    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        print("TOKEN EXPIRED!")
        return render_template_string("""
            <script>window.location.href = "/login";</script>
        """), 401

    @jwt.invalid_token_loader
    def invalid_token_callback(err_msg):
        print("INVALID TOKEN!")
        return render_template_string("""
            <script>window.location.href = "/login";</script>
        """), 422