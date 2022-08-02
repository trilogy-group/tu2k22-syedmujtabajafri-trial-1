from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message44": "Hello World"}

@app.get("/welcome")
async def validate(name: str = ""):
    return {"message2": "Welcome " + name}
