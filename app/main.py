from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
from config.model import genai_model

app = FastAPI()
#==============

import google.generativeai as genai


def flash_model():
    """Create a flash model using Google Generative AI."""
    genai.configure(api_key=GOOGLE_API_KEY)
    return genai.GenerativeModel('gemini-1.5-flash')

genai_model = flash_model()

@app.get("/")
def get():
    return {"message": "Hello World!"}

@app.get("/hello")
def get_hello(query: str= Form(...)):
    try:
        response = genai_model.generate_content(query)
        return {"message": response.text}
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
