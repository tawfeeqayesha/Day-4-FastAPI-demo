
from fastapi import FastAPI

app = FastAPI()

# Endpoint 1: Welcome message
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI application!"}

# Endpoint 2: Greet a person using a path parameter
@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}! Congratulations on using FastAPI."}

# Endpoint 3: Get information using a query parameter
@app.get("/info")
def get_info(course: str = "Python"):
    return {"message": f"You are learning {course}."}