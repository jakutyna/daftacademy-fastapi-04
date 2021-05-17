from fastapi import FastAPI
from .routers import northwind

app = FastAPI()
app.include_router(northwind.router)


@app.get("/")
def index():
    return {"message": "Hello!"}
