from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    a: int
    b: int


@app.get("/")
async def root():
    return {"message45": "Hello World"}

@app.get("/welcome")
async def validate(name: str = ""):
    return {"message222": "Welcome " + name}

@app.post("/sum/")
async def sum(item: Item):
    print(item.a)
    print(item.b)
    return {
        "sum": "1"
    }