from fastapi import FastAPI

from src.routes import contact, auth

app = FastAPI()

app.include_router(auth.router, prefix='/api')
app.include_router(router=contact.router)

@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}
