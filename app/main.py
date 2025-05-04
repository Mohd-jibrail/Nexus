from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.auth import authentication_router

app = FastAPI()

@app.get("/")
def get():
    return {"message": "Hello World!"}

@app.get("/hello")
def get_hello():
    return JSONResponse(content={"message": "Hello Jibrail!"}, status_code=200)

app.include_router(authentication_router, prefix="/api/v1/auth", tags=["auth"])