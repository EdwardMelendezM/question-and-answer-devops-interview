from typing import Union
import os.path
from fastapi import FastAPI

app = FastAPI()

PATH = "/etc/message.txt"

@app.get("/")
def read_root():
    message = "Hello World"
    if os.path.isFile(PATH):
        f = open(PATH, "r")
        message = f.read()
    return {"Hello": message}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}