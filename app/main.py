from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def get():
    return {"message": "Hello World!"}

@app.get("/hello")
def get_hello():
    return JSONResponse(content={"message": "Hello Jibrail!"}, status_code=200)
