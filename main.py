from fastapi import FastAPI
from typing import TypedDict
app = FastAPI()

@app.get("/")
def return_details():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }