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
    """
    The startup function is called when the application starts up.
    It's a good place to initialize things that are needed by your app,
    like connecting to databases or initializing caches.

    :return: A dictionary of functions and objects that will be shared between all the requests
    :doc-author: Trelent
    """
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
    """
    The custom_middleware function is a middleware function that adds the time it took to process
    the request in seconds as a header called 'performance'

    :param request: Request: Get the request object
    :param call_next: Call the next middleware in the chain
    :return: A response object with a new header
    :doc-author: Trelent
    """
    start_time = time.time()
    response = await call_next(request)
    during = time.time() - start_time
    response.headers['performance'] = str(during)
    return response


@app.get("/api/healthchecker")
def root():
    """
    The root function returns a JSON object with the message &quot;Welcome to FastAPI!&quot;


    :return: A dictionary
    :doc-author: Trelent
    """
    return {"message": "Welcome to FastAPI!"}


app.include_router(auth.router, prefix='/api')
app.include_router(router=contact.router)
app.include_router(users.router, prefix='/api')
