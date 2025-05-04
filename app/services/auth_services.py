from schemas.auth_schema import SignUp, SignIn

def validate_sign_up(sigIn: SignUp):
    if not sigIn.email or not sigIn.password:
        return False, "Email and password are required."
    if len(sigIn.password) < 6:
        return False, "Password must be at least 6 characters long."
    if not sigIn.username:
        return False, "Username is required."
    return True, None

def validate_sign_in(sigIn: SignIn):
    if not sigIn.email or not sigIn.password:
        return False, "Email and password are required."
    if len(sigIn.password) < 6:
        return False, "Password must be at least 6 characters long."
    return True, None
def sign_in(user: SignIn):
    try:
        is_valid, error_message = validate_sign_in(user)
        if not is_valid:
            return {"error": error_message}, 400
        return {"message": "Sign in route"}, 200
    except Exception as e:
        return {"error": str(e)}, 500