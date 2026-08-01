from fastapi import FastAPI
from typing import TypedDict
app = FastAPI()

@app.get("/")
def return_details():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

class Tasks(TypedDict):
    id: int
    title: str
    done: bool
tasks=[
    Tasks(id=1,title='solve homework',done=False),
    Tasks(id=2,title='get groceries', done=True),
    Tasks(id=3, title='work out', done=False)
]



@app.get("/tasks")
def return_tasks():
    return tasks

@app.get("/tasks/{req_id}")
def return_task_id(req_id: int):
    if req_id is None or req_id not in (task.get('id') for task in tasks):
        return { "error": "Task 99 not found" }
    else:
        return (task for task in tasks if task["id"]==req_id)
@app.get("/health")
def return_health():
    return {'status':"OK"}