import os
import subprocess
from pathlib import Path

def run_command(command):
    subprocess.run(command, shell=True, check=True)

def create_file(path, content=""):
    with open(path, "w") as f:
        f.write(content)

def main():
    print("Setting up FastAPI project...")

    # Create folders
    os.makedirs("app/routers", exist_ok=True)
    os.makedirs("app/models", exist_ok=True)
    os.makedirs("app/schemas", exist_ok=True)

    # Create virtual environment
    print("Creating virtual environment...")
    # run_command("python -m venv venv")

    # Install dependencies
    print("Installing dependencies...")
    run_command("pip install --upgrade pip")
    run_command("pip install fastapi uvicorn python-dotenv sqlalchemy pydantic")

    # Write requirements.txt
    requirements = "\n".join(["fastapi", "uvicorn", "python-dotenv", "sqlalchemy", "pydantic"])
    create_file("requirements.txt", requirements)

    # Write .env file
    create_file(".env", "# Add environment variables here")

    # Write README.md
    create_file("README.md", "# FastAPI Project")

    # Write app/main.py
    main_py = '''from fastapi import FastAPI
from app.routers import example

app = FastAPI()

app.include_router(example.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI project"}
'''
    create_file("app/main.py", main_py)

    # Write app/routers/example.py
    example_py = '''from fastapi import APIRouter

router = APIRouter()

@router.get("/hello")
def say_hello():
    return {"message": "Hello from router"}
'''
    create_file("app/routers/example.py", example_py)

    print("Setup complete. Activate your virtual environment and run: uvicorn app.main:app --reload")

if __name__ == "__main__":
    main()