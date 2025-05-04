from fastapi import APIRouter
from fastapi.responses import JSONResponse
from services.auth_services import validate_sign_up
from schemas.auth_schema import SignUp, SignIn

authentication_router = APIRouter()

@authentication_router.get("/signup")
def sign_in(user: SignUp):
    try:
        is_valid, error_message = validate_sign_up(user)
        if not is_valid:
            return JSONResponse(content={"error": error_message}, status_code=400)
        return JSONResponse(content={"message": "Sign Up route"}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@authentication_router.get("/signin")
def sign_up():
    return JSONResponse(content={"message": "Sign up route"}, status_code=200)

@authentication_router.get("/signout")
async def signout():
    return JSONResponse(content={"message": "Sign out route"}, status_code=200)