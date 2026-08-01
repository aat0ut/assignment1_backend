from fastapi import FastAPI
from typing import TypedDict
app = FastAPI()

@app.get("/")
def hello_world():
    return "hello world"