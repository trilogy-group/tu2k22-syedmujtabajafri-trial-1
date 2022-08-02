from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message45": "Hello World"}

@app.get("/welcome")
async def validate(name: str = ""):
    return {"message222": "Welcome " + name}
