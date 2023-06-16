from fastapi import FastAPI

from src.routes import contact

app = FastAPI()

app.include_router(router=contact.router)
@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}
