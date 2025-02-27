from os import name
from fastapi import responses
from fastapi import websockets
from fastapi.exceptions import HTTPException
from fastapi.responses import PlainTextResponse
from starlette.responses import HTMLResponse
from exceptions import StoryException
from fastapi import FastAPI
from router import blog_get, blog_post, user, article, product, file
from auth import authentication
from templates import templates
from db import models
from db.database import engine
from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import time
from client import html
from fastapi.websockets import WebSocket

app = FastAPI()
app.include_router(templates.router)
app.include_router(authentication.router)
app.include_router(file.router)
app.include_router(user.router)
app.include_router(article.router)
app.include_router(product.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)


# @app.get("/hello")
# def index():
#     return {"message": "Hello World"}


@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code=418,
        content={"detail": exc.name}
    )

@app.get("/")
async def get():
  return HTMLResponse(html)

clients = []

@app.websocket("/chat")
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  clients.append(websocket)
  while True:
    data = await websocket.receive_text()
    for client in clients:
      await client.send_text(data)


# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=400)


# Create the database tables
models.Base.metadata.create_all(engine)

origins = [
  'http://localhost:3000'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins = origins,
  allow_credentials = True,
  allow_methods = ["*"],
  allow_headers = ['*']
)

app.mount('/files', StaticFiles(directory="files"), name='files')
app.mount('/templates/static',
      StaticFiles(directory="templates/static"),
      name="static"
)