from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    a: int
    b: int


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/welcome")
async def validate(name: str = ""):
    return {"message": "Welcome " + name}

@app.post("/sum/")
async def sum(item: Item):
    return {
        "sum": item.a + item.b
    }