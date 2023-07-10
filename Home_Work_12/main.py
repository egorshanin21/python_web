import time

import redis.asyncio as redis
from fastapi import FastAPI, Request, Depends
from fastapi_limiter import FastAPILimiter

from starlette.middleware.cors import CORSMiddleware

from src.routes import contact, auth, users
from src.conf.config import settings

app = FastAPI()


@app.on_event("startup")
async def startup():
    r = await redis.Redis(host=settings.redis_host, port=settings.redis_port, db=0)
    await FastAPILimiter.init(r)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def custom_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    during = time.time() - start_time
    response.headers['performance'] = str(during)
    return response


@app.get("/api/healthchecker")
def root():
    return {"message": "Welcome to FastAPI!"}


app.include_router(auth.router, prefix='/api')
app.include_router(router=contact.router)
app.include_router(users.router, prefix='/api')
